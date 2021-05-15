# 프로젝트 9주차

(2021.05.15 19:00 ~ 23:00)

***

# 학습 내용

***

* django 기초 학습
    + [django 공식 홈페이지의 튜토리얼 1~7장 실습](https://docs.djangoproject.com/ko/3.2/intro/tutorial01/)
    ![image](https://cdn.discordapp.com/attachments/820225658969915406/843116389531385856/2021-05-15_10.23.22.png)
    ![image](https://media.discordapp.net/attachments/820225658969915406/843118067797590016/2021-05-15_10.30.05.png)
    ![image](https://cdn.discordapp.com/attachments/820225658969915406/843118144775913522/2021-05-15_10.30.21.png)  
    ![image](https://cdn.discordapp.com/attachments/820225658969915406/843118786118811678/2021-05-15_10.32.55.png)
    ![image](https://media.discordapp.net/attachments/820225658969915406/843119241653125151/2021-05-15_10.34.44.png?width=1077&height=348)      


* REST API 개념 학습
  

    + "REpresentational State Transfer"의 줄임말
      + 자원을 이름(자원의 표현)으로 구분하여 해당 자원의 상태(정보)를 주고 받는 모든 것을 의미   
        => 자원(resource)의 표현(representation)에 의한 상태 전달
    + 월드 와이드 웹(www)과 같은 분산 하이퍼미디어 시스템을 위한 소프트웨어 개발 아키텍처의 한 형식   
      => 웹의 기존 기술과 HTTP 프로토콜을 그대로 활용하기에 웹의 장점을 최대한 활용할 수 있는 아키텍처 스타일
    
    + HTTP URL을 통해 자원을 명시하고, HTTP Method(POST, GET, PUT, DELETE)를 통해 해당 자원에 대한 CRUD Operation을 적용하는 것을 의미함
    
    + REST API : REST 아키텍처의 제약 조건을 준수하는 애플리케이션 프로그래밍 인터페이스를 뜻함
    
    + REST 구성요소 : 자원(URL), 행위(HTTP Method), 표현(Representation of Resource)

    + Rest 특징 : 서버-클라이언트 구조, 무상태, 캐시 처리가능, 계층화, Code-On-Demand, 인터페이스 일관성
  
    + REST 장점 : HTTP 프로토콜의 인프로 그대로 사용하므로 별도의 인프라 구축할 필요 없음, HTTP 표준 프로토콜에 따르는 모든 플랫폼에서 사용 가능,
                 REST API 메세지가 의도하는 바를 명확하게 나타내므로 의도하는 바 쉽게 파악 가능, 서버와 클라이언트의 역할 명확하게 분리함 등
    + REST 단점 : 표준이 존재하지 않음, 사용할 수 있는 메소드가 4가지 밖에 없음, 구형 브라우저가 아직 제대로 지원해주지 못하는 부분들 존재 등

## 다음 주
- REST API 설계 및 구현 예정...