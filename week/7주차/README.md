# 프로젝트 7주차

(2021.04.25 14:00 ~ 18:10)

***

# 학습 내용
- 학습된 모델을 저장 
- 저장한 모델을 불러와서 임의의 사진을 통해 테스트 진행       
    ex)![image](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Team_Korea_Russia_WorldCup_02_%28cropped%29.png/200px-Team_Korea_Russia_WorldCup_02_%28cropped%29.png)
- 이미지 텐서에 대한 이해
    ![image](https://cdn.discordapp.com/attachments/820225658969915406/835772671450808330/2021-04-25_4.02.08.png)     

- 결과의 정확도 개선을 위한 방법 시도
    데이터 전처리 방법 변경하여 추가 학습
        - transforms.RandomRotation(30)
            정확도 약 57%
            ![image](https://cdn.discordapp.com/attachments/820225658969915406/835798120486404096/unknown.png)

- 결과의 인덱스값들 백분율로 표현하기
    양수와 음수로 섞여 나오는 인덱스 값들 => 백분율로 표현하여 가독성 높이기
    ![image](https://media.discordapp.net/attachments/820225658969915406/835800732028239882/2021-04-25_5.53.38.png)
    ![image](https://cdn.discordapp.com/attachments/820225658969915406/835800866727788554/2021-04-25_5.54.11.png)
    ![image](https://cdn.discordapp.com/attachments/820225658969915406/835801443179954186/2021-04-25_5.56.30.png)

***
# 결과
input   
![image](https://imgnn.seoul.co.kr/img/upload/2015/05/07/SSI_20150507184218_V.jpg)       

output   
![image](https://media.discordapp.net/attachments/820225658969915406/835801278650122259/unknown.png)
***

## 다음 주
- API 설계 방안 토론
. . .