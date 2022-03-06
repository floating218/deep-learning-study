# Tensorflow2.0, Keras기반으로 모델링하는 방법 간단 정리

## 파일 구성
```
data/
model/
ㄴModel.py
Loader.py
Metric.py
Run.py
```

## Run.py에 들어가는 내용
- Run 클래스 정의
  - init 함수에서 Loader호출해서 인풋 데이터 준비해두기
  - run 함수 에서 Model호출해서 모델 인스턴스 생성하고 준비된 인풋 데이터로 fit시키기
  - 그 외 다른 metric 호출하는 함수 넣기
- `if __name__=="__main__":`
  - parse_args()처리
  - Run 인스턴스 생성 후 어떤 함수를 어떤순서로 호출할지 결정

## Loader.py에 들어가는 내용
- Loader 클래스 정의
- 정해진 file_path를 가지고 데이터 읽기
- 학습에 맞는 형태로 데이터 변경 (pandas 패키지 활용)

## Model.py에 들어가는 내용
- keras 가이드 참고
- Model 클래스 정의
  - init에서 레이어를 정의하고 연결
  - .get_model()로 모델 리턴하게 함




