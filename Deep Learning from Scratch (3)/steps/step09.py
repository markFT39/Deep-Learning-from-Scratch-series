import numpy as np

class Variable:
    def __init__(self, data):
        if data is not None:
            if not isinstance(data, np.ndarray):
                raise TypeError('{}은(는) 지원하지 않습니다.'.format(type(data)))

        self.data = data
        self.grad = None
        self.creator = None

    def set_creator(self, func):
        self.creator = func

    def backward(self):
        if self.grad is None:
            self.grad = np.ones_like(self.data)

        funcs = [self.creator]
        while funcs:
            f = funcs.pop() # 함수를 가져온다
            x, y = f.input, f.output    # 함수의 입력과 출력을 가져온다
            x.grad = f.backward(y.grad) # backward 메서드를 호출한다

            if x.creator is not None:
                funcs.append(x.creator) # 하나 앞의 함수를 리스트에 추가한다

def as_array(x):
    if np.isscalar(x):
        return np.array(x)
    return x

class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)     # 구제척인 계산은 forward에서 진행
        output = Variable(as_array(y))  # numpy의 데이터 타입 변환 문제 개선
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

def square(x):
    return Square()(x)  # 함수 호출 방식을 변경해 파이썬 함수 지원

def exp(x):
    return Exp()(x)

if __name__ == '__main__':
    x = Variable(np.array(0.5))
    y = square(exp(square(x)))
    y.backward()
    print(x.grad)

    x = Variable(np.array(1.0))
    x = Variable(None)
    x = Variable(1.0)           # TypeError 발생