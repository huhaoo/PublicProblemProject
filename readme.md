### Todolist

- [x] 支持atcoder
- [x] 去重
- [x] 模块化
- [x] skydogli 卷榜
- [ ] CraZYali 支持codeforces (c.py/c.out)
- [ ] pengzhike 支持loj (l.py/l.out)

```python3
from mail import mail
from ins import ins
```

`mail(s)`可以发送字符串`s`至邮箱

`ins(s)`可以检查`s`是否在`ins.out`中，若在，返回$0$，否则将`s`加入`ins.out`末尾（不换行），并返回$1$。

注意将`__pycache__/`加入`.gitignore`中。
