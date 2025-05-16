# Files
Here I will list usefull files, inputs that can be played with. What can be expected as output.

### ./input_slim/**kakapo_1_bottleneck.slim**

**Important inputs:** (are defined in the script, but can be played with)

 - effectDel1: There is currently 1 mutation. This is its deletriusness (selection coeff.)
 - MU: Mutation rate. Currently set to what Jarno calculated for Kakapo x10
 - K_initialise: The carrying capacity K during the initialisation phase.
 - phase1_initialise_length: The length (simulation steps) of the phase 1 period.
 - K_bottleneck: The carrying capacity K during the bottleneck phase.
 - phase2_bottleneck_length: The length (simulation steps) of the phase 2 period.
 - K_recovery: The carrying capacity K during the recovery phase.
 - phase3_recovery_length: The length (simulation steps) of the phase 3 period.

**Expected output:**

During the simulation (every step): `'simulation cycle': 'population size' ('oldest individual'), mean age: ['mean age']`

After the simulation: example
```
--END OF RUN--
Fitness after phase 1: 0.84863
Fitness after phase 2: 1.01883
Fitness after phase 3: 0.850157
Final phase 1 population size: 4493
Final phase 2 population size: 39
Final phase 3 population size: 3939
```
You can use the tag `--END OF RUN--` to just gather the final data.

### ./input_slim/**kakapo_2_bottleneck.slim**

**Important inputs:** (are defined in the script, but can be played with)

 - effectDel1: There is currently 1 mutation. This is its deletriusness (selection coeff.)
 - MU: Mutation rate. Currently set to what Jarno calculated for Kakapo x10
 - K_initialise: The carrying capacity K during the initialisation phase.
 - phase1_initialise_length: The length (simulation steps) of the phase 1 period.
 - K_bottleneck: The carrying capacity K during the bottleneck phase.
 - phase2_bottleneck_length: The length (simulation steps) of the phase 2 period.
 - K_recovery: The carrying capacity K during the recovery phase.
 - phase3_recovery_length: The length (simulation steps) of the phase 3 period.
 - phase4_bottleneck_length: The length (simulation steps) of the phase 4 period.
 - phase5_recovery_length: The length (simulation steps) of the phase 5 period.

**Expected output:**

During the simulation (every step): same as before.

After the simulation: example
```
--END OF RUN--
Fitness after phase 1: 0.872061
Fitness after phase 2: 0.987138
Fitness after phase 3: 0.859289
Fitness after phase 4: 0.70662
Fitness after phase 5: 0.840119
Final phase 1 population size: 4487
Final phase 2 population size: 40
Final phase 3 population size: 3943
Final phase 4 population size: 33
Final phase 5 population size: 2985
```
You can use the tag `--END OF RUN--` to just gather the final data.

### ./input_slim/**kakapo_3_bottleneck.slim**

same as kakapo_2_bottleneck.slim but then with another bottleneck -> recovery sequence.

### ./input_slim/**kakapo_merge.slim**

**Important inputs:** (are defined in the script, but can be played with)

 - effectDel1: There is currently 1 mutation. This is its deletriusness (selection coeff.)
 - MU: Mutation rate. Currently set to what Jarno calculated for Kakapo x10
 - K_population2: The carrying capacity (is constant) of the second population.
 - K_initialise: The carrying capacity K during the initialisation phase.
 - phase1_initialise_length: The length (simulation steps) of the phase 1 period.
 - K_bottleneck: The carrying capacity K during the bottleneck phase.
 - phase2_bottleneck_length: The length (simulation steps) of the phase 2 period.
 - K_recovery: The carrying capacity K during the recovery phase.
 - phase3_recovery_length: The length (simulation steps) of the phase 3 period.
 - phase4_bottleneck_length: The length (simulation steps) of the phase 4 period.
 - phase5_recovery_length: The length (simulation steps) of the phase 5 period.

 
During the simulation (every step): same as before.

After the simulation: example
```
--END OF RUN--
Fitness after phase 1: 0.859254
Fitness after phase 2: 0.835717
Fitness after phase 3: 0.856347
Final phase 1 population size: 4469
Final phase 2 population size: 37
Final phase 3 population size: 4530
P2 Fitness after phase 1: 0.854047
P2 Fitness after phase 2: 0.849202
P2 Fitness after phase 3: NULL
P2 Final phase 1 population size: 4492
P2 Final phase 2 population size: 4440
P2 Final phase 3 population size: 0
```
You can use the tag `--END OF RUN--` to just gather the final data.

### ./input_slim/**kakapo_migrants.slim**

**Important inputs:** (are defined in the script, but can be played with)

 - effectDel1: There is currently 1 mutation. This is its deletriusness (selection coeff.)
 - MU: Mutation rate. Currently set to what Jarno calculated for Kakapo x10
 - K_population2: The carrying capacity (is constant) of the second population.
 - migrate_count: The amount of individuals that will get migrated from P2 to P1
 - K_initialise: The carrying capacity K during the initialisation phase.
 - phase1_initialise_length: The length (simulation steps) of the phase 1 period.
 - K_bottleneck: The carrying capacity K during the bottleneck phase.
 - phase2_bottleneck_length: The length (simulation steps) of the phase 2 period.
 - K_recovery: The carrying capacity K during the recovery phase.
 - phase3_recovery_length: The length (simulation steps) of the phase 3 period.
 - phase4_bottleneck_length: The length (simulation steps) of the phase 4 period.
 - phase5_recovery_length: The length (simulation steps) of the phase 5 period.

 
During the simulation (every step): same as before.

After the simulation: example
```
--END OF RUN--
Fitness after phase 1: 0.85966
Fitness after phase 2: 0.711595
Fitness after phase 3: 0.865821
Final phase 1 population size: 4528
Final phase 2 population size: 33
Final phase 3 population size: 4481
P2 Fitness after phase 1: 0.868467
P2 Fitness after phase 2: 0.861613
P2 Fitness after phase 3: 0.847849
P2 Final phase 1 population size: 4535
P2 Final phase 2 population size: 4540
P2 Final phase 3 population size: 4515
```
You can use the tag `--END OF RUN--` to just gather the final data.
