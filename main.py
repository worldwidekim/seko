from movie_title_review import *
import re


if __name__ == "__main__":
    title_result = get_daum_movie_title(2725)
    print(title_result)
    review_result = get_daum_movie_review(2725, 2)
    print(review_result)

    review_number_result = get_daum_movie_review_number(2725, 2)
    result = re.search('\((.*)\)', review_number_result)
    print(result.group(1))

