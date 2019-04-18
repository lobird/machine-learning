# Gradient descend 的三种方式

## 普通方式

该方式任何时候都使用相同的速度进行梯度下降。其公式为:

$$
w_{n+1}=w_{n} - \eta \frac{\partial J(\theta)}{\partial \theta}
$$

## Vanilla Gradient Descend (香草GD？)

该方式的$\eta​$值是变化的，即：$\eta ^t = \frac{\eta}{\sqrt{t+1}}​$

$$
w_{n+1}=w_{n} - \eta^t \frac{\partial J(\theta)}{\partial \theta}
$$


## Adagrad

仍然是改变$\eta$
值，
令：$\eta ^t = \frac{\eta}{\sqrt{\sum_{i=0}^{t}{g^i}} }$

然后继续带入计算$w_{n+1}$,即可。
