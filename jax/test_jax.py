import timeit
import jax.numpy as jnp
from jax import grad, jit, vmap
from jax import random

def selu(x, alpha=1.67, lmbda=1.05):
    return lmbda * jnp.where(x > 0, x, alpha * jnp.exp(x) - alpha)

key = random.PRNGKey(0)
x = random.normal(key, (1000000,))
timeit.timeit('selu(x).block_until_ready()', globals=globals())
