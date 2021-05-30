# 프로젝트 11주차

(2021.05.30 19:00 ~ 22:30)

***

# 학습 내용

***

* REST API 완성하기

```python
class Face(models.Model):
    content = models.TextField()

    @property
    def result(self):
        return face.do(self.content)

    def __str__(self):
        return '{}'.format(self.result)
```

![image](https://media.discordapp.net/attachments/820225658969915406/848518582190604288/2021-05-30_8.09.50.png?width=720&height=394)

+ 문제점   
  -POST 전송시 => 계속해서 데이터가 쌓임 // 데이터를 저장하여 사용하는 구조가 아니기에 POST로 입력 받은 데이터를 저장할 필요 없음   
=> 해결방안) Signals 사용   
```python
@receiver(post_save, sender=Face)
def face_post_save(sender, instance, **kwargs):
    instance.delete()  
```

+ POST로 데이터 전송
```python
import requests
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("base64_string.txt") as f:
    data = f.read()

param = {}

param["content"] = data

url = "http://localhost:8000/api/face/"

response = requests.post(url, param).json()

print(response['result'])
```
![image](https://cdn.discordapp.com/attachments/820225658969915406/848549963260362792/unknown.png)
[참고](https://hongku.tistory.com/292)

## 다음 주
- Spring 서버 구상...