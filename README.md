# NaiveBayes_STM32
This Repository Provide the a simple code for Naive bayes Classifier Implementation in STM32L0538-DISCO board.

Clock Frequency Used: 16 MHz

The project implements Naive Bayes Classifier with CMSIS DSP library in Keil U5. 
High clock frequency gives high performance also consumes more power.
Hence the 16 MHz clock frequency is used as it is neither low clock frequency, nor high clock frequency.
This project implements Naive Bayes classifier using CMSIS DSP in STM32.
arm_gaussian_naive_bayes_predict_f32 function is used for performing the Naive Bayes estimator. The 16 MHz clock helps to perform the 
computation using this function quickly. 
Furthermore the peripherals like UART,ADC,SPI,I2C are usually driven by a clock derived from the system clock. Hence when the application is developed further
the 16 MHz clock will enable the peripherals to operate at high speed.

Timer-6 Peripheral is enabled with period of 10ms inorder to perform the Naive Bayes computation every 10ms.

Code Flow:
Naive Bayes classifier is a probabilistic classifier based on bayes theorem.
It assumes independence between attributes of data points.
The key insight of Bayes' theorem is that the probability of an event can be adjusted as new data is introduced.

The Code is developed on a STM32L0 Series Cortex -M0+ 32-bit Microcontroller.
 - clock is configured to 16 MHz and the initialization is done in the firmware by SystemClock_Config().
 - Timer (TIM 6) is initialized with prescalar 15999 and period to 10ms.
 - Gaussian Naive Bayes classifier is used and the model is trained using sikit learn in python and the resultanat parameteres are used for CMSIS-DSP.
 - The interface structure and paramter variables are declared and defined.
 - The timer is initialized and when the counter counts up for 10ms the timer interrupt kicks in and the Timer_INTFLAG is set to "1".
 - In main the Timer_INTFLAG is checked if it is set to high ('1'), if yes then the timer is stopped and " arm_gaussian_naive_bayes_predict_f32"  function is invoked with necessary parameters passed as arguments.
 - The "arm_gaussian_naive_bayes_predict_f32" return the class of the parameteres passed which is stored in a variable class.
 - Once the predcited class is obtained the Timer_INTFLAG is set to '0' and the Timer start function is called.
 
 The python code file (NB .py) is also uploaded to the repository.
 
 
