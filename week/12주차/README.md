# 프로젝트 12주차

(2021.06.06 19:00 ~ 22:00)

***

# 학습 내용

***

## `Spring Boot` 웹 프로젝트 설계

* 간단한 프로토타입 페이지 생성

페이지에서 얼굴 이미지를 업로드 받아서 `Django` 서버에 HTTP POST 요청 전송

## 오류 발생

__HTTP POST 요청시 아래와 같은 에러 발생__

> 400 Bad Request: [{"content":["Not a valid string."]}]]

* 원인

```python
class FaceSerializer(serializers.ModelSerializer):
    content = serializers.CharField(required=True)
```

Django 서버의 serializer에서 Char값을 받아오고 있었는데 계속해서 자바에서 JSON 형식으로 HTTP POST 요청을 보내서 발생되는 오류였다.

* 해결

`serializers.JSONField 로 변경`

```python
class FaceSerializer(serializers.ModelSerializer):
    content = serializers.JSONField(required=True)
```

* [https://stackoverflow.com/questions/50374192/not-a-valid-string-error-when-trying-save-dict-to-textfield-in-django-rest](https://stackoverflow.com/questions/50374192/not-a-valid-string-error-when-trying-save-dict-to-textfield-in-django-rest)

## 구현

```java
    @PostMapping("/image")
    public String imageUpload(MultipartFile image) throws IOException {

        StringBuilder sb = new StringBuilder();
        sb.append(StringUtils.newStringUtf8(Base64.encodeBase64(image.getBytes(), false)));

        MultiValueMap<String, String> params = new LinkedMultiValueMap<>();
        params.add("content", "test");
        log.info(sb.toString());

        HttpHeaders headers = new HttpHeaders();
        headers.add("Content-Type", "application/json");
        headers.add("Accept", "application/json");
        headers.add("Accept-Encoding", "gzip, deflate, br");

        HttpEntity<MultiValueMap<String, String>> entity = new HttpEntity<>(params, headers);

        RestTemplate rt = new RestTemplate();

        try {
            ResponseEntity<String> response = rt.exchange(
                    "http://localhost:8000/api/face/",
                    HttpMethod.POST,
                    entity,
                    String.class
            );
            log.info(response.getBody());
        } catch (Exception e) {
            log.warn(e.toString());
        }

        return "redirect:/test/image";
    }
```

* HTTP 요청 결과

```java
{"content":["test"],"result":[14,12,14,15,15,16,11]}
```

## 다음 주
- 스프링 웹 페이지 완성
- 캠을 통한 웹페이지에서 실시간 이미지 전송 방법 찾기 & 구현