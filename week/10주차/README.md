# 프로젝트 10주차

(2021.05.23 19:00 ~ 23:00)

***

# 학습 내용

***

* Django REST framework

![image](https://user-images.githubusercontent.com/69145799/119262496-6ed9c500-bc16-11eb-9184-007819a0433f.png)

![image](https://cdn.discordapp.com/attachments/820225658969915406/846020769590673458/2021-05-23_10.44.23.png)

## post.user" must be a "user" instance. 에러

* 원인

POST 메소드 데이터 입력 권한을 없애서 익명 유저(AnonymousUser) 에게도 POST가 가능하도록 설정했는데
post 객체가 생성될 때 user 값이 null 이라서 발생하였다.

* 해결 방법

1. POST 권한을 User 에게만 준다.
2. models.py에 Post 클래스의 속성 중 user 에 null=True 값을 추가해준다.

## API 설계 방향 (두가지 서버로 구성)
1. Django REST API 서버(pytorch 모델 연산 수행)
2. Spring boot 서버(thymeleaf front view)

## 서비스 연계 순서
1. 사용자가 스프링 부트 서버 웹페이지에 접속
2. 이미지 파일을 업로드(추후에 웹캠과 연동하여 자동으로 이미지 업로드 예정)
3. 업로드된 이미지를 base64 인코딩으로 변환하여 REST API 서버로 전송
4. 학습한 pytorch 모델을 이용하여 이미지의 표정 판별
5. 결과 값 스프링 부트 서버로 전송
6. 사용자에게 표정 판별 결과 제공

## 다음 주
- Django 서버 이미지 판별 요청 GET 메소드로 매핑하기(Post 클래스 수정)
- Serializer.py 수정
- import face.py
- REST API 완성하기