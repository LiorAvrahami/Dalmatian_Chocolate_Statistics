*theory will be done for wight balls, other colors are simaler.

# analising distribution of single ball

## mass of single ball

### basic theory
denote W = the random variable, that corresponds to the mass of a single white ball.

denote w = the random variable, that corresponds to the total mass of all the white balls in a single pack.

denote n = the random variable, that corresponds to the total number of white balls in a single pack.

denote S = the set of measurments: {(ni,wi) | where both ni and wi are both measurements of n and w}, where n corrisponds to the number of white balls in the measurment, and w corrisponds to the weight of the wight balls in the measurment.

$$
E[W] = \frac{\text{total mass of all measurments in S}}{\text{total number of balls in all measurments in S}} = \frac{\sum\limits_{i}{w_i}}{\sum\limits_{i}{n_i}}
$$

but I want to know more about W, my oproch will be to assume some distribution for W and se if it coinsides with the measurments in S.

### statistical measurments

||
|:---:|
|![](group_mass_vs_group_size%20distributions_for_different_groups_of_balls.png)|
|description|

### assumptions on distrebution of M

#### M is uniformly distributed, 

so M ~ U[a,b], 

#### idea for assumption: the subdistrebution of M in a spesific pack

the subdistrebution of M in a spesific pack depends only on the total mass of balls in the pack, so:

denote T = the random variable, that corresponds to the total mass of balls in a single pack. (this variable sums over all colors, so for a pack with 2gr black balls, 4gr brown balls and 1gr white ball, T would be 7gr).

justification: the distribution of M might change if information regarding the other balls in the pack is added to the system. this is mostly because it is aperant from the basic statistics, that the total mass of the balls in a pack is almost fixed ($Var(mw + mb + mk) < Var(mw) + Var(mb) + Var(mk)$). but, assuming the differant ball colors have similar size distrebutions, and assuming the balls are mixed outside the container and then placed in the pack, the color of the other balls in the pack shouldn't affect the size of a singled out ball. so it makes sense to only allow M to depend on (T-M)

