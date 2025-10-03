if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from dezero import Variable

def f(x):
    y = x ** 4 - 2 * x ** 2
    return y


if __name__ == '__main__':
    x = Variable(np.array(2.0))
    y = f(x)
    # 첫 번째 미분
    y.backward(create_graph=True)
    print(x.grad)

    gx = x.grad
    x.cleargrad()
    # 두 번째 미분
    gx.backward()
    print(x.grad)


    # 뉴턴 방법을 통한 최적화
    x = Variable(np.array(2.0))
    iters = 10

    for i in range(iters):
        print(i, x)

        y = f(x)
        x.cleargrad()
        y.backward(create_graph=True)

        # 두 번째 이상의 역전파(미분) 진행
        gx = x.grad
        x.cleargrad()
        gx.backward()
        gx2 = x.grad

        # 뉴턴 방법을 통한 계산 결과 갱신 (최솟값 찾기)
        x.data -= gx.data / gx2.data