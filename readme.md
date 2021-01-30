## Todolist

- [x] 支持atcoder
- [x] 去重
- [x] 模块化
- [ ] skydogli 卷榜
- [x] 支持codeforces
- [ ] pengzhike 支持loj (l.py/l.out)

## 文件调用指令

注意将`__pycache__/`加入`.gitignore`中。

### Mail

```python
from mail import mail
```

可调用`mail(s)`发送字符串`s`至邮箱

### Insert

```python
from ins import ins
```

可调用`ins(s)`检查`s`是否在`ins.out`中，若在，返回$0$，否则将`s`加入`ins.out`末尾（不换行），并返回$1$。

`ins.out`使用格式：题号+`_`+人名，每次空一格

### a.py/c.py/l.py

```python
import a
import c
import l
```

各个文件需要提供接口`Get(name)`函数，传入提交者id，返回其`AC submission`的字符串，具体格式为：

```python
2xxx-xx-xx xx:xx:xx name Accepted problem_id
2xxx-xx-xx xx:xx:xx name Accepted problem_id
```

### run.py

自动调用各OJ文件，并整合后统一发送
