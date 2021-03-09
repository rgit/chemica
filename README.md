<h1>Chemica</h1>
<h4>A simple library that takes chemistry to the next level 👨‍🔬🔬🥽🧪🧬</h4>


<h2>Installation:</h2>
<h6>Download the latest version of the library using pip</h6>

```bash
$ pip3 install chemica -U
```


<h2>Usage examples:</h2>

<h5>Solving equation:</h5> 

```python3
from chemica import Chemica

print(Chemica.solve("CuCl2", "Zn"))
```

<h6>This example will return this equation object:</h6>

```python3
Equation(substances=('CuCl2', 'Zn'), result='CuCl2(aq) + Zn(s) → Cu(s) + ZnCl2(aq)')
```

<br>

<h5>Getting info about substance:</h5>

```python3
from chemica import Chemica

print(Chemica.info("Zn"))
```

<h6>This example will return this substance object:</h6>

```python3
Substance(substance='Zn', name='Zinc, Zinc powder (pyrophoric), Zn, Element 30, 30Zn, Cinc, Zink, Zn(ii), Zn2+, Zincum, Blue powder', condition='Grey-to-blue powder')
```


<h2>License</h2>
<p>The library is under the MIT license.</p>
<p>
    Read the <a href="https://github.com/mishailovic/chemica/blob/main/LICENSE">LICENSE</a> for more information.
</p>