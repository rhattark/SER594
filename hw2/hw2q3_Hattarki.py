import yaml
import datetime
import pickle

__author__ = "Rhishabh Hattarki"
__date__ = "21 September 2023"
__assignment = "SER594: Homework 2 Q3"


def gradescope_preprocessor(input_filename, output_filename):
    """
    See homework assignment.
    :param input_filename: Filename for YAML Gradescope metadata.
    :param output_filename: Filename for pickle processed data.
    """

    max_score = 0

    with open(input_filename, 'r') as submission_file:
        try:
            submission = yaml.safe_load(submission_file)
            
            for _, sub_data in submission.items():
                sub_total_score = 0
                test_count = 0

                for test in sub_data[':results']['tests']:
                    sub_total_score += test['max_score']
                    test_count += 1

                max_score = sub_total_score if sub_total_score > max_score else max_score
                break

            print('ASSIGNMENT INFO:')
            print(f'Max score possible: {max_score}')
            print(f'Number of criteria: {test_count}')

        except yaml.YAMLError as error:
            print(error)


if __name__ == '__main__':
    filename = "hw2q3_submission_metadata.yml"
    filename_out = "hw2q3_gradescope_processed.pickle"
    gradescope_preprocessor(filename, filename_out)
