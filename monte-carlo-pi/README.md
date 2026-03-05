# Monte Carlo Method: Theory and Application

The **Monte Carlo method** is a powerful computational technique that relies on **random statistical sampling** to solve complex **deterministic problems** or to simulate systems characterized by significant uncertainty.

Instead of relying solely on analytical mathematical formulas, which can be difficult or impossible to solve for complex systems, this method performs **thousands or millions of random experiments** to approximate a final value or behavior.

### The Three Main Pillars
1.  **Random Generation**: Generate a large set of random inputs following a specific probability distribution.
2.  **Deterministic Execution**: Perform a specific calculation or simulation for each individual random input.
3.  **Results Aggregation**: Average the obtained results to find the expected value, a specific constant (like $\pi$), or the final probability of an event.

## Practical Example: Estimating $\pi$

The script `pi.py` provides a classic example of the Monte Carlo method used to estimate the value of $\pi$.

### Mathematical Logic
Consider a circle of radius $r = 1$ inscribed within a square. Based on geometric principles, the relationship between their areas is:

$$\frac{A_{circle}}{A_{square}} = \frac{\pi r^2}{(2r)^2} = \frac{\pi(1)^2}{4(1)^2} = \frac{\pi}{4}$$



### Algorithmic Implementation
By generating a massive number of random points within the square, we can approximate the ratio of the areas by counting how many points fall inside the circle. 

Assuming `totalTests` represents the total points generated in the square and `correctTests` represents those that fall inside the circle, we have:

$$\frac{A_{circle}}{A_{square}} \approx \frac{correctTests}{totalTests}$$

For each iteration, we determine if a point $(x, y)$ is inside the circle using the following system:

$$ \text{isInsideCircle?} = 
\begin{cases} 
\text{true}, & \sqrt{x^2 + y^2} \le 1 \\ 
\text{false}, & \text{otherwise} 
\end{cases} 
$$

### Final Calculation
By combining the formulas above, we can conclude that:

$$\pi \approx 4 \cdot \frac{correctTests}{totalTests}$$

**The larger** the number of tests performed, **the closer** the estimated output will be to the actual mathematical value of $\pi$ ($\approx 3.14159$).