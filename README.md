


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

| Target: `star_type`   | Star Class            | Description             |
| :-------------------- | :-------------------- | :---------------------- |
| 0                     | Red Dwarf             | Smallest, longest burning (life), lowest temperature star. <br> "A red dwarf, which is half as massive as the sun, can last 80 to 100 billion years, which is far longer than the universe's age of 13.8 billion years. This long lifetime is one reason red dwarfs are considered to be good sources for planets hosting life, because they are stable for such a long time." <br>[red-dwarf](https://www.space.com/23772-red-dwarf-stars.html)                       | 
| 1                     | Brown Dwarf            | Star that cannot sustain nuclear fusion in their cores. Considered a transitional object between a star and a planet. <br> [brown-dwarf](https://cdn.mos.cms.futurecdn.net/K4FXX56wkmoU8Urex2KuNV-970-80.jpg.webp)| 
| 2                     | White Dwarf       | Star that runs out of hydrogen and helium and collapses inward on itself. <br> White dwarfs are incredibly dense. "According to NASA, the gravity on the surface of a white dwarf is 350,000 times that of gravity on Earth. That means a 150-pound (68-kilogram) person on Earth would weigh 50 million pounds (22.7 million kg) on the surface of a white dwarf." <br> [white-dwarf](https://www.space.com/23756-white-dwarf-stars.htm) | 
| 3                     | Main Sequence     | Main sequence stars fuse hydrogen atoms to form helium atoms in their cores. About 90 percent of the stars in the universe, including the sun, are main sequence stars. These stars can range from about a tenth of the mass of the sun to up to 200 times as massive. <br> [main-sequence](https://www.space.com/22437-main-sequence-stars.html)           | 
| 4                     | Super Giants      | Supergiant stars have two colors: red and blue. Supergiants are the most massive stars out there, ranging between 10 to 70 solar masses, and can range in brightness from 30,000 to hundreds of thousands of times the output of the Sun. They have very short lifespans, living from 30 million down to just a few hundred thousand years. Supergiants seem to always detonate as Type II supernovae at the end of their lives. <br> [super-giants](https://www.universetoday.com/25325/supergiant-star/)           | 
| 5                     | Hyper Giants      | The largest stars in the universe. Hypergiant stars were first identified separately from other supergiants because they are significantly brighter; that is, they have a larger luminosity than others. Studies of their light output also show that these stars are losing mass very rapidly. That "mass loss" is one defining characteristic of a hypergiant. The others include their temperatures (very high) and their masses (up to many times the mass of the Sun) <br> [hyper-giants](https://www.thoughtco.com/hypergiant-stars-behemoths-of-the-galaxy-3073593)           | 

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
| quantiled_temperature          | MinMaxScaled Temperature scaled using a QuantileTransformer                                 |
| quantiled_luminosity           | MinMaxScaled Luminosity scaled using a QuantileTransformer                                  |
| quantiled_radius               | MinMaxScaled Radius scaled using a QuantileTransformer                                      |
| quantiled_absolute_mangnitude  | MinMaxScaled Absolute Magnitude scaled using a QuantileTransformer                          |


## Project Steps
### 1. Acquire
- Stars dataset acquired from [Kaggle](https://www.kaggle.com/brsdincer/star-type-classification)
- Created a function called `get_star_data()` make data acquisition reproducible.
- Temperature, Luminosity, Radius, and Absolute Magnitude are non-normally distributed.


### 2. Prepare
- Created a function called `prep_star_data()` to clean the dataset.
- Lowercase column names for easier data manipulation.
- Rename ambiguous column names with descriptive names.
- Map `star_type` numeric id's with their actual star name in a column called `star_type_name`.
- Convert the datatype of the `spectral_class`, and `color` to categorical.
- Clean and normalize the text in the `color` column.
- Drop the unscaled columns: `temperature`, `luminosity`, `radius`. and `absolute_magnitude`
- Rearrange columns.

**Feature Engineering**
- Created scaled columns of `temperature`, `luminosity`, `radius`. and `absolute_magnitude` using a MinMaxScaler.
- Created quantiled columns of the MinMaxScaled versions of `temperature`, `luminosity`, `radius`. and `absolute_magnitude` using a QuantileTransformer.
- Dropped the `luminosity` column from the dataset because `absolute_magnitude` is the measure of a star's luminosity, irregardless of the distance in space.

**Preprocessing**
- The data splits: Train 50%, Validate 37.5%, Test 12.5%
- Stratified by `star_type`

### 3. Explore
- Created a heatmap of correlations between continuous features and `star_type`.
- Created 3 pairplots to visualize the interactions between continuous features.
- Created a 3D scatterplot of the three most visually separable features.
- Created a 2D scatterplot of `absolute_magnitude` and `star_type`.
- Created a violinplot to understand the distribution of continuous features across `star_type`.
- Created 3 crosstab heatmaps to map the interactions between categorical features.
- Created a parallel plot visualize the `star_type` and `spectral_class` using `absolute_magnitude` to indicate luminosity (brightness).

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

__Is a star's type dependent on spectral class?__
> 𝐻0: `Star type` is independent of `spectral class`.
>
> 𝐻1: `Star type` is dependent on `spectral class`.
>
> Outcome: Reject the null hypothesis
<br>

__Is a star's type dependent on color?__
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
- Baseline Model Accuracy is 23%
- Decision Tree Model Accuracy is 100%
- The Decision Tree Model outperformed the Baseline by 329%

- The most important features in determining `star_type` is `absolute_magnitude`(scaled) and `radius` (quantiled).

![tree](./visuals/tree.png)

### 5. Conclusion
__New stars we observe can be classified by knowing their `absolute_magnitude` and `radius`.__

### 6. Future Investigations
- Given the small size of the dataset, I wonder if new stars would impact the prediction capability of the model.


## How to Reproduce
All files are reproducible and available for download and use.
- [x] Read this README.md
- [ ] Clone this repository
- [ ] Run Final-Report.ipynb
