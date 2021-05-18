![star-header](./visuals/stars_header.png)

![executive-summary](./visuals/executive_summary.png)


## Background
https://www.eso.org/public/usa/news/eso1615/


## Data Dictionary
 
**`stars.csv`**
| Feature Name                                  | Description                                                                   |
| :-------------------------------------------- | :---------------------------------------------------------------------------- |
| Temperature                                   | Temperature in Kelvin                                                         |
| Relative Luminosity                           | Amount of light emitted by an object in a unit of time. <br>`Relative Luminosity = Luminosity / Luminosity of the Sun` <br> [luminosity-wiki](https://en.wikipedia.org/wiki/Luminosity)|
| Relative Radius                               | Radius of a star <br>`Relative Radius = Radius / Radius of the Sun`                                   |
| Absolute Magnitude                            | Luminosity of a celestial object, on an _inverse logarithmic astronomical magnitude scale_. <br> <br> The absolute magnitude of a star is equal to the apparent magnitude that the object would have if it were viewed from a distance of exactly 10 parsecs (32.6 light-years), without extinction of its light due to absorption by interstellar matter and cosmic dust. By hypothetically placing all objects at a standard reference distance from the observer, _their luminosities can be directly compared among each other on a magnitude scale_. <br> [absolute-magnitude-wiki](https://en.wikipedia.org/wiki/Absolute_magnitude)                                                            |
| Color                                         | Red, Orange Red, Orange, Pale Yellow Orange, Yellow White, White, Blue White, Blue. "The surface temperature of a star determines the color of light it emits".                                                  |
| Spectral Class                                | O,B,A,F,G,K,M <br> [spectral-wiki](https://en.wikipedia.org/wiki/Stellar_classification)  |

| Target Name           | Description             |
| :-------------------- | :---------------------- |
| 0 : Red Dwarf         | Smallest, longest burning (life), lowest temperature star. <br> "A red dwarf, which is half as massive as the sun, can last 80 to 100 billion years, which is far longer than the universe's age of 13.8 billion years. This long lifetime is one reason red dwarfs are considered to be good sources for planets hosting life, because they are stable for such a long time." <br>[red-dwarf](https://www.space.com/23772-red-dwarf-stars.html)                       | 
| 1 : Brown Dwarf       | Star that cannot sustain nuclear fusion in their cores. Considered a transitional object between a star and a planet. <br> [brown-dwarf](https://cdn.mos.cms.futurecdn.net/K4FXX56wkmoU8Urex2KuNV-970-80.jpg.webp)| 
| 2 : White Dwarf       | Star that runs out of hydrogen and helium and collapses inward on itself. <br> White dwarfs are incredibly dense. "According to NASA, the gravity on the surface of a white dwarf is 350,000 times that of gravity on Earth. That means a 150-pound (68-kilogram) person on Earth would weigh 50 million pounds (22.7 million kg) on the surface of a white dwarf." <br> [white-dwarf](https://www.space.com/23756-white-dwarf-stars.htm) | 
| 3 : Main Sequence     | Main sequence stars fuse hydrogen atoms to form helium atoms in their cores. About 90 percent of the stars in the universe, including the sun, are main sequence stars. These stars can range from about a tenth of the mass of the sun to up to 200 times as massive. <br> [main-sequence](https://www.space.com/22437-main-sequence-stars.html)           | 
| 4 : Super Giants      | Supergiant stars have two colors: red and blue. Supergiants are the most massive stars out there, ranging between 10 to 70 solar masses, and can range in brightness from 30,000 to hundreds of thousands of times the output of the Sun. They have very short lifespans, living from 30 million down to just a few hundred thousand years. Supergiants seem to always detonate as Type II supernovae at the end of their lives. <br> [super-giants](https://www.universetoday.com/25325/supergiant-star/)           | 
| 5 : Hyper Giants      | The largest stars in the universe. Hypergiant stars were first identified separately from other supergiants because they are significantly brighter; that is, they have a larger luminosity than others. Studies of their light output also show that these stars are losing mass very rapidly. That "mass loss" is one defining characteristic of a hypergiant. The others include their temperatures (very high) and their masses (up to many times the mass of the Sun) <br> [hyper-giants](https://www.thoughtco.com/hypergiant-stars-behemoths-of-the-galaxy-3073593)           | 

<details><summary>Click here for a deep dive into the data dictionary</summary>
 
#### Kelvin scale 
|                | From kelvins               | To kelvins                  |
| :------------- | :------------------------- | :-------------------------- |
| Celsius        | 	[°C] = [K] − 273.15 	  | [K] = [°C] + 273.15         |
| Fahrenheit     | 	[°F] = [K] × 9⁄5 − 459.67 |	[K] = ([°F] + 459.67) × 5⁄9 |

 On the Kelvin scale, pure water freezes at 273.15 K, and it boils at 373.15 K.
 [source](https://en.wikipedia.org/wiki/Kelvin)


#### Spectral Class

![spectral-visual](./visuals/spectral_classes.jpg)


MATH:

    1 Solar Luminosity = 3.828 x 10^26 Watts [Average Luminosity of the Sun]

    1 Solar Radius = 6.9551 x 10^8m [Average Radius of the Sun]

</details>

### Feature Engineering
| Feature Name                   | Description                                                                                 |
|:------------------------------ |:------------------------------------------------------------------------------------------- |
| scaled_temperature             | Temperature scaled using a MinMaxScaler                                                     |
| scaled_luminosity              | Luminosity scaled using a MinMaxScaler                                                      |
| scaled_radius                  | Radius scaled using a MinMaxScaler                                                          |
| scaled_absolute_mangnitude     | Absolute Magniutde scaled using a MinMaxScaler                                              |
| quantiled_temperature          | MinMaxScaled Temperature scaled using a Quantile Transformer                                |
| quantiled_luminosity           | MinMaxScaled Luminosity scaled using a Quantile Transformer                                 |
| quantiled_radius               | MinMaxScaled Radius scaled using a Quantile Transformer                                     |
| quantiled_absolute_mangnitude  | MinMaxScaled Absolute Magnitude scaled using a Quantile Transformer                         |


## Project Steps
### 1. Acquire
Acquire Takeaways
- Stars dataset acquired from Kaggle:
- Created a function called get_star_data() in the src package.
- Temperature, Luminosity, Radius, and Absolute Magnitude are non-normally distributed.


### 2. Prepare
- Created a function named prep_star_data() to clean the dataset.
- Lowercase column names for easier data manipulation.
- Rename ambiguous column names with descriptive names.
- Map star_type numeric id's with their actual star name in a column called star_type_name
- Convert the datatype of the spectral_class, and color to categorical and create coded versions of these columns.
- Clean and normalize the text in the color column.
- Drop the unscaled columns: temperature, `
- Rearrange columns.

**Feature Engineering**

**Preprocessing**
- The data was split using a 50%-37.5%-12.5% method. Stratifying the splits by the target variable `star_type` means that each `star_type` is split 20-15-5, 40 stars for each of the 6 classes.

### 3. Explore


#### Hypotheses
__Do Super Giants, Main Sequence, Brown Drawfs, and Red Dwarfs have significantly different radii?__
> 𝐻0: The average `quantiled radius` of each star is equal to the population mean.
> 
> 𝐻1: The average `quantiled radius` of each star is significantly different than the population mean.
>
> Outcome: Reject the null hypothesis
<br>

__Is the average radius of each star type significantly different from another?__
> 𝐻0: The average `quantiled radius` of __Super Giants__ and __Main Sequence__ Stars is equal.
>
> 𝐻1: The average `quantiled radius` of __Super Giants__ and __Main Sequence__ Stars is significantly different.
>
> Outcome: Reject the null hypothesis
<br>

> 𝐻0: The average `quantiled radius` of __Super Giants__ and __Brown Dwarfs__ is equal.
>
> 𝐻1:The average `quantiled radius` of __Super Giants__ and __Brown Dwarfs__ is significantly different.
>
> Outcome: Reject the null hypothesis
<br>

> 𝐻0: The average `quantiled radius` of __Super Giants__ and __Red Dwarfs__ is equal.
>
> 𝐻1: The average `quantiled radius` of __Super Giants__ and __Red Dwarfs__ is significantly different.
>
> Outcome: Reject the null hypothesis
<br>

> 𝐻0: The average `quantiled radius` of __Main Sequence__ and __Brown Dwarfs__ is equal.
>
> 𝐻1: The average `quantiled radius` of __Main Sequence__ and __Brown Dwarfs__ is significantly different.
>
> Outcome: Reject the null hypothesis
<br>

> 𝐻0: The average `quantiled radius` of __Main Sequence__ and __Red Dwarfs__ is equal.
>
> 𝐻1:The average `quantiled radius` of __Main Sequence__ and __Red Dwarfs__ is significantly different.
>
> Outcome: Reject the null hypothesis
<br>

> 𝐻0: The average `quantiled radius` of __Brown Dwarfs__ and __Red Dwarfs__ is equal.
>
> 𝐻1: The average `quantiled radius` of __Brown Dwarfs__ and __Red Dwarfs__ is significantly different.
>
> Outcome: Reject the null hypothesis
<br>

> 𝐻0: The `average quantiled` radius of __Hyper Giants__ and __White Dwarfs__ is equal.
> 
> 𝐻1: The `average quantiled` radius of __Hyper Giants__ and __White Dwarfs__ is significantly different.
>
> Outcome: Reject the null hypothesis
<br>

__Is a star's type dependent on the spectral class?__
> 𝐻0: `Star type` is independent of `spectral class`.
>
> 𝐻1: `Star type` is dependent on `spectral class`.
>
> Outcome: Reject the null hypothesis
<br>

__Is a star's type dependent on its color?__
> 𝐻0: `Star type` is independent of `color`.
> 
> 𝐻1: `Star type` is dependent on `color`.
>
> Outcome: Reject the null hypothesis
<br>

__Is spectral class dependent on color?__
> 𝐻0: `Star type` is independent of `color`.
> 
> 𝐻1: `Star type` is dependent on `color`.
>
> Outcome: Reject the null hypothesis
<br>

### 4. Model
![tree](./visuals/tree.png)

### 5. Conclusion
A star can be classified using its `absolute_magnitude` and `radius`.

#### Key Findings

## How to Reproduce
All files are reproducible and available for download and use.
- [x] Read this README.md
- [ ] Download the aquire.py, prepare.py, and Final-Report.ipynb files
- [ ] Run Final-Report.ipynb
