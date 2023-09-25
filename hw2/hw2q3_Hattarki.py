import yaml
import datetime
import pickle

__author__ = "Rhishabh Hattarki"
__date__ = "21 September 2023"
__assignment = "SER594: Homework 2 Q3"

class ValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)

def gradescope_preprocessor(input_filename, output_filename):
    """
    See homework assignment.
    :param input_filename: Filename for YAML Gradescope metadata.
    :param output_filename: Filename for pickle processed data.
    """

    max_score = 0
    criterias = []
    name_to_num_max = dict()

    def validate_same_assess(sub_data):
        if len(name_to_num_max) != len(sub_data[':results']['tests']):
            return False
        
        for test in sub_data[':results']['tests']:
            if test['name'] not in name_to_num_max:
                return False
            num_max = name_to_num_max[test['name']]
            if num_max['number'] != test['number'] or num_max['max_score'] != test['max_score']:
                return False
        return True

    with open(input_filename, 'r') as submission_file:
        try:
            submission = yaml.safe_load(submission_file)
            
            for _, sub_data in submission.items():
                sub_total_score = 0
                test_count = 0

                for test in sub_data[':results']['tests']:
                    sub_total_score += test['max_score']
                    test_count += 1
                    criterias.append(test['name'])
                    name_to_num_max[test['name']] = {
                        'number': test['number'],
                        'max_score': test['max_score']
                    }

                max_score = sub_total_score if sub_total_score > max_score else max_score
                break

            print('ASSIGNMENT INFO:')
            print(f'Max score possible: {max_score}')
            print(f'Number of criteria: {test_count}')
            print(f'Criteria: {criterias}')
            print(f'Number of submitters: {len(submission)}')
            print()

            for _, sub_data in submission.items():
                if (not validate_same_assess(sub_data)):
                    raise ValidationError('Submission did not match rubric schema.')

                for submitter in sub_data[':submitters']:
                    submitter_name = submitter[':name']
                    submitter_sid = submitter[':sid']
                    print(f'{submitter_name} ({submitter_sid})')

                dates_and_scores = []

                for old_sub in sub_data[':history']:
                    if (not validate_same_assess(old_sub)):
                        raise ValidationError('Submission did not match rubric schema.')
                    dates_and_scores.append((old_sub[':created_at'], old_sub[':score']))
                dates_and_scores.append((sub_data[':created_at'], sub_data[':score']))

                if len(dates_and_scores) > 1:
                    date_diff = dates_and_scores[-1][0] - dates_and_scores[0][0]
                    print(f'\tsubmitted {len(dates_and_scores)} times over {date_diff}')
                elif len(dates_and_scores) == 1:
                    print(f'\tsubmitted 1 time')

                for date_, score_ in dates_and_scores:
                    print(f'\tsubmission at {date_} earned {score_}')

        except yaml.YAMLError as error:
            print(error)
        except ValidationError as error:
            print(error)


if __name__ == '__main__':
    filename = "hw2q3_submission_metadata.yml"
    filename_out = "hw2q3_gradescope_processed.pickle"
    gradescope_preprocessor(filename, filename_out)
