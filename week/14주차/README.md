# 프로젝트 14주차

(2021.06.20 19:00 ~ 23:30)

***
# 학습 내용

## 문제 해결

* numpy array에서 dimension을 추가하는 방법

```python
cropped_img = np.expand_dims(
            np.expand_dims(cv2.resize(d, (48, 48)), 0), 0
        )
## 이전 [48, 48]
## 결과 [1, 1, 48, 48]
```

> ndarray에서 dimension을 추가할 때 매개변수 | 0 = 앞에 추가 / -1 = 뒤에 추가 |

* runtimeerror: expected scalar type byte but found float 에러

```python
cropped_img = torch.from_numpy(cropped_img).float()
```

> ndarray에서 Tensor로 변환하여 predict를 수행하는데 FloatTensor 가 아니라서 발생한 오류
> .float()을 통해 간단히 Tensor -> FloatTensor로 변환해주었다.

## 얼굴 인식 추가

`haarcascade_frontalface_default.xml` 이용하여 얼굴 인식 후 이미지에서 얼굴 프레임만 잘라서 모델에 예측 수행

```python
facecasc = cv2.CascadeClassifier('templates/haarcascade_frontalface_default.xml')

def do(encoded_string):
    encoded_string = encoded_string[0]

    decoded = np.asarray(bytearray(base64.b64decode(encoded_string)), dtype=np.uint8)
    decoded = cv2.imdecode(decoded, cv2.IMREAD_COLOR)
    decoded = cv2.cvtColor(decoded, cv2.COLOR_BGR2GRAY)
    face = facecasc.detectMultiScale(decoded, scaleFactor=1.3, minNeighbors=5)
    print(face)
    for (x, y, w, h) in face:
        d = decoded[y:y + h, x:x + w]
        cropped_img = np.expand_dims(
            np.expand_dims(cv2.resize(d, (48, 48)), 0), 0
        )
        cropped_img = torch.from_numpy(cropped_img).float()
        out = model(cropped_img)  # predict
        p = out.tolist()
        print(p)
        lis = out.flatten().tolist()
        lis = list(map(lambda x: x + 100, lis))
        result = [int(round(a / sum(lis), 3) * 100) for a in lis]
        classes = ['neutral', 'fearful', 'sad', 'happy', 'surprised', 'angry', 'disgusted']

        print("표정 :", classes)
        print("확률 :", result)

        maxindex = int(np.argmax(p))
        print("결과 :", classes[maxindex])

        return result
```

## 매 초마다 결과 그래프 업데이트

```js
var getData = function () {
        context.drawImage(video,0,0,960,720);
        var image = canvas.toDataURL('image/png');
        $('#image').val(image);
        $.ajax({
            type: "post",
            data: $('#image'),
            url: "/test/image",
            error: function () {
                alert("fail!");
            },
            success: function (data) {
                try {
                    console.log(data);
                    for (var i=0; i<8; i++) {
                        myChart.data.datasets[0].data[i] = data[i];
                    }
                    myChart.update();
                } catch (e) {
                    alert(e);
                }
            }
        })
    };

    setInterval(getData, 1000);
```

## 완성

![image](https://user-images.githubusercontent.com/69145799/121810231-ef7e6500-cc9a-11eb-9ec8-11c8991f4028.png)

이전 주차에서 작성한 페이지에서 그래프 레이블들의 값을 매 초마다 업데이트 하도록 수정하여 완성하였다.


# 마무리하며

구현하기로 계획했던 모든 기능들을 구현하는데 성공했지만 학습 모델의 정확도가 기대치만큼 높지 않아서 아쉬웠다. 

48x48 이미지로는 사람의 모든 표정을 정확히 예측하기는 어려운것 같다!

더 높은 해상도의 학습용 이미지 데이터들을 통하여 모델을 학습시키면 조금더 좋은 결과를 얻을 수 있을 것 같다.

# 참고자료  
* [얼굴인식하여 cropping 하기](https://deepflowest.tistory.com/149)   
* [OpenCV 실시간 얼굴 인식](https://velog.io/@sidcode/파이썬-OpenCV로-실시간-얼굴-인식하기)
