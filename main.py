from movie_title_review import *
import re


# 이렇게 모든 함수는 moview_title_review.py 에 넣고 그 함수를 돌릴 스크립을 따로 만들어서 (main.py) 돌리는게 정석
if __name__ == "__main__":
    title_result = get_daum_movie_title(2725)
    print(title_result)
    review_result = get_daum_movie_review(2725, 2)
    print(review_result)

    # get_daum_moview_reivew_number 제대로 돌아가는데 거기에 숫자가 () 사이에 나오니까 아래 있는 re (regular expression) 써서 그거만 지워줬음.
    review_number_result = get_daum_movie_review_number(2725, 2)
    result = re.search('\((.*)\)', review_number_result)
    print(result.group(1))

