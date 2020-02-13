from sklearn import svm

#XOR 계산데이터
#2차원 리스트로 정의함 리스트 내부에 있는 리스트의 요소는 차례대로 입력 P,Q와 답을 나타냅니다.
xor_data=[
    #P,Q,result
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

#학습을 위해 데이터와 레이블 분리하기
#학습시키기 위한 데이터 변수 , 정답레이블변수 로 나눔
#scikit-learn 의 머신러닝을 수행할때 사용하는 fit() 메서드의 매개변수를 맞추기 위함입니다.
data = [] 
label = []
for row in xor_data:
    p=row[0]
    q=row[1]
    r=row[2]
    data.append([p,q])
    label.append(r)
#데이터 학습시키기
#SVM 객체를 만들고 , fit()메서드를 사용해 데이터를 학습시킵니다.
#fit 메서드 첫번째 변수는  학습할 데이터 배열 ,두번쨰 변수는 결과
clf = svm.SVC()
clf.fit(data,label)

#데이터 예측하기
pre = clf.predict(data)
print(pre)

#결과 확인하기
ok = 0 ; total = 0
for idx,answer in enumerate(label):
    p= pre[idx]
    if p == answer: ok+=1
    total += 1
print("correct rate:",ok,"/",total,"=",ok/total)