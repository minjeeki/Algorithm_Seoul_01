# 그리디 (Greedy) 알고리즘

## 그리디 알고리즘이란?

* 문제에 대해서 단순 무식하게, 탐욕적으로(매 단계마다 가장 좋아보이는 것만을 선택해서) 푸는 알고리즘

  * ex. 배열의 최댓값을 구할 때, 배열의 첫번째 수를 가장 큰 값이라고 가정하고 이후 값들을 살펴볼 때 현재 가장 큰 값과 비교 후 업데이트하는 상황

* 현재의 선택이 나중에 미칠 영향에 대해서는 고려하지 않음

  => 정확한 답을 도출하지 못하더라도 그럴싸한 답을 도출 (최적해)

  => 그리디 알고리즘을 사용해도 되는 상황인지, 정당성을 고민하며 해결 방안을 떠올려야 함

* 기준에 따라 좋은 것을 선택하는 것이기에 기준을 제시해줌

  * ex. '가장 큰 순서대로', '가장 작은 순서대로'

  * 정렬 알고리즘을 사용했을 때 기준을 만족시킬 수 있는 경우가 많음

  => 정렬 알고리즘과 짝을 이뤄 출제되는 경우가 많음

## 그리디 알고리즘의 특징

* 다른 유형 (정렬, 최단 경로 등) 대비 사전에 외우고 있지 않아도 풀 수 있는 가능성이 높은 문제 유형

* 출제 폭이 넓은 문제 유형

  => 단순 암기를 통해 모든 문제를 대처하기는 어려움

  => 많은 유형을 접해보고 문제를 풀어보며 훈련이 필요함

* 보통 코딩 테스트에서 출제되는 그리디 알고리즘의 유형은 창의력(문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력)을 요구한다.

  => 단순히 현재 상황에서 가장 좋아보이는 것만을 선택해도 문제를 풀 수 있는지 파악할 수 있어야 함

* 다양한 알고리즘에서 두루 사용 (ex. 다익스트라 최단 경로, 크루스칼 알고리즘)

## 그리디 알고리즘의 정당성

> "대부분의 문제는 그리디 알고리즘을 이용했을 때 최적의 해를 찾을 수 없는 가능성이 다분하다. 따라서 그리디 알고리즘으로 문제의 해법을 찾았을 때는 해법의 정당성을 검토해야 한다"

* 문제 풀이를 위한 최소한의 아이디어를 떠올리고 아이디어가 정당한지 검토할 수 있어야 한다

* 문제를 만났을 때 유형 파악이 어렵다면, 그리디 알고리즘을 의심하고 탐욕적인 해결법이 존재하는지 고민 필요 -> 그리디로 못찾을 경우 DP나 그래프 알고리즘을 고민해볼 것

  * 여러개의 테스트 케이스를 기반으로 패턴을 찾으려고 해보자

## 레퍼런스

* '이것이 취업을 위한 코딩테스트다 with 파이썬' 86 ~ pg