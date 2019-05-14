MIT가 2013년을 빛낼 10대 혁신기술 중 하나로 선정하고 가트너(Gartner, Inc.)가 2014 세계 IT 시장 10대 주요 예측[6] 에 포함시키는 등 최근들어 딥 러닝에 대한 관숨이 높아지고 있지만 사실 딥 러닝 구조는 인공신경망(ANN, artificial neural networks)에 기반하여 설계된 개냠으로 역사를 따지자면 최소 1980년 Kunihiko Fukushima에 의해 소개 된 Neocognitron 까지 거슬러 올라가야 한다.

1989년에 얀 르쿤과 그의 동료들은 오류역전파 알고리즘(backpropagation algorithm)에 기반하여 우편물에 손으로 쓰여진 우편번호를 인식하는 deep neural networks를 소개 했다. 알고리즘이 성공적으로 동작했음에도 불구하고, 신경망 학습에 소요되는 시간(10 개의 숫자를 인식하기 위해 학습하는 시간)이 거의 3일이 걸렸고 이것은 다른분야에 일반적으로 적용되기에는 비현실적인 것으로 여겨졌다.

많은 요소들이 느린 속도에 원인을 제공했는데, 그 중 하나는 1991년 Jürgen Schmidhuber의 제자였던 Sepp Hochreiter에 의해 분석된 vanishing gradient problem(지역최솟값에 머무르게 되는 원인)이었다[10][11]. 또한 불연속 시뮬레이션에서 초기 상태를 어떻게 선택하느냐에 따라 수렴이 안되고 진동 또는 발산하는 문제, 트레이닝셋에 너무 가깝게 맞추어 학습되는 과적합 (Overfitting) 문제, 원론적으로 생물학적 신경망과는 다르다는 이슈들이 끊임 없이 제기되면서 인공신경망은 관심에서 멀어졌고 90년대와 2000년대에는 서포트 벡터 머신 같은 기법들이 각광받게 된다.

본격적으로 딥 러닝이란 용이를 사용한 것은 2000년대 딥 러닝의 중흥기를 이끌어간다고 평가할 수 있는 제프리 힌튼[12] 과 Ruslan Salakhutdinov에 의해서이며, 기존 신경망의 과적합 문지를 해결하기 위해 이들은 unsupervised RBM(restricted Boltzmann machine)을 통해 학습시킬 앞먹임 신경망(Feedforward Neural Network)의 각 층을 효과적으로 사전훈련(pre-trainning)하여 과적합을 방지할 수 있는 수준의 initialize point를 잡았고, 이를 다시 supervised backpropagation를 사용[13]하는 형태로 학습으 진행한다.

또한 2013년에는 신호처리학회인 ICASSP에서 RBM을 대체하여 과적합을 방지할 수 있는 Drop-out[14] 이라는 개념이 소가되면서 사전훈련보다 훨씬 더 간단하고 강력한 형태로 과적합을 방지할 수 있게 되었다.
