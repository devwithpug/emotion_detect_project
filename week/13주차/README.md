# 프로젝트 13주차

(2021.06.13 19:00 ~ 23:00)

***
# 학습 내용
***

## 웹 페이지 제작
1. 페이지에 WebRTC 라이브러리를 이용한 실시간 캠 화면 페이지에 표시하기
2. 캠 화면 캡쳐하여 스프링 서버에 POST 요청
```jquery-css
if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
   navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
        var video = document.getElementById('video');
        video.srcObject = stream;
        // video.play();
    });
}

var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');
var video = document.getElementById('video');
document.getElementById("webcamBtn").addEventListener("click",function() {
    context.drawImage(video,0,0,960,720);
    // console.log(canvas.toDataURL('image/png'));
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
            } catch (e) {
                alert(e);
            }
        }
    })
});
```
3. 결과 그래프로 출력 (미완성)
```jquery-css
var ctx = document.getElementById('myChart');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['neutral', 'fearful', 'sad', 'happy', 'surprised', 'angry', 'disgusted'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3, 90],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(238,220,207,0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgb(64,120,44)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
```
![image](https://user-images.githubusercontent.com/69145799/121810231-ef7e6500-cc9a-11eb-9ec8-11c8991f4028.png)

## 시행착오
1. JQuery, Ajax를 처음 다뤘기에 POST 요청을 구현하는데 상당 시간 소요 
2. CSS, HTML 정렬 및 배치 관련 지식 부족으로 상당 시간 소요

## 참고자료
[웹캠 사용하기](https://ddochi-dev.tistory.com/entry/HTML-웹캠-사용하기)
[JQuery, Ajax](http://blog.naver.com/PostView.nhn?blogId=kkforgg&logNo=220358259789)
[차트 그래프](https://coding-restaurant.tistory.com/65)

## 다음 주
- 결과 출력 그래프 연동
- 특정 시간마다(ex 3초) 결과를 자동으로 출력 