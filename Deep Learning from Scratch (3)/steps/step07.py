import numpy as np

class Variable:
    def __init__(self, data):
        self.data = data
        self.grad = None
        self.creator = None

    def set_creator(self, func):
        self.creator = func

    def backward(self):
        # 함수 가져오기
        f = self.creator
        if f is not None:
            # 함수의 입력 가져오기
            x = f.input
            # 함수의 backward 메서드 호출
            x.grad = f.backward(self.grad)
            # 하나 앞 변수의 backward 메서드 호출로 재귀 실행
            x.backward()

class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)     # 구제척인 계산은 forward에서 진행
        output = Variable(y)
        output.set_creator(self)    # 출력 변수에 창조자(부모 함수)를 기억
        self.input = input      # 입력 변수를 기억
        self.output = output    # 출력 변수를 기억
        return output
    
    def forward(self, x):
        raise NotImplementedError()
    
    def backward(self, gy):
        raise NotImplementedError()
    
class Square(Function):
    def forward(self, x):
        return x ** 2
    
    def backward(self, gy):
        x = self.input.data
        gx = 2 * x * gy
        return gx

class Exp(Function):
    def forward(self, x):
        return np.exp(x)
    
    def backward(self, gy):
        x = self.input.data
        gx = np.exp(x) * gy
        return gx

def f(x):
    A = Square()
    B = Exp()
    C = Square()
    return C(B(A(x)))

if __name__ == '__main__':
    A = Square()
    B = Exp()
    C = Square()

    x = Variable(np.array(0.5))
    a = A(x)
    b = B(a)
    y = C(b)

    y.grad = np.array(1.0)
    y.backward()
    print(x.grad)