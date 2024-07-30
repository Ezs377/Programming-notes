---  
An embedded system is a combination of hardware and software used to perform specific functions. Embedded systems are usually limited resources, reactive, time-constrained, and part of a larger system. Code should be short and concise, peripherals need to be properly configured, interrupts need to be prioritized and short.  

### Microcontroller:  
![[Pasted image 20230814020438.png]]  
![[Pasted image 20230814020504.png]]  
Microprocessor is a CPU, microcontroller uses microprocessor as its CPU alongside other parts.  

![[Pasted image 20230814020622.png]]
This is a collection of logic gates compiled in such a way that we can alter their behaviour through software to perform specific functions (no memory).  Software describes how the hardware is connected, NOT directly executed as commands. We basically alter the behaviour of the circuit with software.  

A microcontroller is more favored for this course since it's easier to use  
![[Pasted image 20230814020855.png]]

Important aspects of microcontroller:  
- Computational power: A measure of how fast the processor can do a task, measured in Millions-of-Instructions-Per-Second (MIPS), higher value is better (e.g. ATmega 328p has 16 MIPS, an i7 intel core has 200000 MIPS). Higher MIPS means more power consumption. Clock speed is related to MIPS by the cycles needed to do one instruction, e.g. If clock is 60 MHz (cycles per second), and it takes 4 clock cycles to do one instruction, then 16 MIPS (note MIPS is in millions)
- Program memory (flash memory): Where code to execute is stored. Usually in kilobytes or megabytes for microcontrollers. More required code means more flash is needed.  
- Random access memory (RAM): Where processed data is stored, and the current state of microprocessor. More data that needs to be stored = more RAM. Usually in kilobytes or megabytes for microchips.  

The I/O peripherals:  
- General Purpose Input Output (GPIO): Reads/generates high/low (digital) signals  
- Universal Asynchronous Receiver Transmitter (UART): Sends and receives binary data using a simple serial protocol (serial cable)
- Analog to Digital Converter (ADC): Converts analog value to digital value (AC signal to digital)  
- Timers: Allows real-time measurements and executing realtime tasks

When selecting a MCU (micro controller unit):  
- Power consumption
- Operating voltage range
- Operating temperature range
- Packages available (size and shape of the chip itself)
- Compiler support
- Development tools needed to use it
- Programming tools needed to use it
- Available software libraries
- Certifications for the chip
- Cost
- Availability
- Lead-time
- Minimum order quantity (MOQ)

The ATmega328P has:  
- 8 bit processor
- 16 MIPS at 16MHz clock
- 32 kb of flash memory
- 2 kb of RAM
- 3 timers
- 8 channel 10-bit SAR type ADC
- USART (UART unit)
- 23 GPIO pins
- Operates between 2.7 v to 5.5 v at a temperature range of -40<sup>o</sup> C to 125<sup>o</sup> C

![[Pasted image 20230814143239.png]]  
The ATmega328P (formally referred to as the MCU from now on) is programmed in C code using Atmel Studio IDE. The ELF file generated during compiling can be used to simulate in Proteus to test code. once verified we can download the ELF or HEX file into MCU program memory.  

### Coding:  

The variable types typically used are:  
![[Pasted image 20230814143918.png]]  
Local variables only work in the function, global works in the whole program. A static variable is reset to zero at the start of runtime and value is kept in a function even after exiting it. Volatile variables ensures compiler doesn't optimize the variable where compiler removes variables it thinks is 'useless'. Extern allows other files to access the variable.  

Example:  
![[Pasted image 20230814144347.png]]  
Notes:  
- For `loc_harry` 300 exceeds the 8 bit limit and hence it will overflow
- For `bad_dev` we get a value of 1 because `loc_tom` is set as 8-bit integer hence can only be used as an integer regardless of the resulting type, so typecasting must be used (shown in `good_dev`)
- For `reslt_is_16bit` we need to convert at least one of the values as 16-bit, otherwise compiler assumes 8-bit calculations and gives wrong answer  
- `glob_tom`, `glob_harry`, `glob_will` will all hold the same value, the 'A' will be converted to its ASCII equivalent, and the other two are hexadecimal and binary equivalents respectively.

To simulate code, go to Project, Properties, Tools, select Simulator in drop-down. Now we can use Start debugging and break button besides the play/pause buttons.  

Left side of screen should be processor status, bottom is flash memory,  
![[Pasted image 20230814161044.png]]

**Operators:**  
![[Pasted image 20230814163810.png]]

Bitwise operators act on individual bits, while logical operators work on variables. THEY ARE DIFFERENT.  
Bitwise operators use single characters and apply the logic to each individual bit, e.g.  
`11 & 10` will compare each bit starting from the right using the AND logic, so in this case we would get (1 & 0), (1 & 1) which gives the result 10 (remember operator starts from the right).  

Right/left shifting will shift by the given number, and replace removed bits with a zero, e.g. (10 << 2) means left shift twice, so we get (10)<--(00), where the 10 is shifted out leaving a binary value of 00.  

**Bitwise:**  
Bitwise operators can be used for masking, i.e. AND operating two bits. Using shifts we can accurately tell which bits we want on and which bits we want off, e.g. 
- In `slctd` we mask the binary value with another binary value that is two shifts with OR mask. 
- In particular, `1<<1` provides us the value of `10`, while `1<<2` gives us value of `100`
- Hence using OR will give us `10 | 100` which in bitwise operation gives `110`. 
- Applying this mask to the original binary gives `00110011 & 00000110` (since we can assume all other bits are zero for the mask) which gives  `00000010` as the final output.  Note that the AND mask takes note of both bits from the original and mask, so if one is 0 and the other one is 1 then it will become 0.  

**Logical:**  
Logical operators use double characters, and essentially compare the values and give either true or false output. Note however that since binary is 1 and 0, which corresponds to true and false, then accidentally doing bitwise can also give a true/false output depending on the binary equivalents of the values compared.  

**Rational:**  
Comparison operators, e.g. `==` for Equals to. This compares the VALUES, not the binary equivalent of the value.  

We can also use `<var>++` to increment a variable value by 1, and `<var>--` to decrement. `+=` also works.  

Control statement usage (e.g. `For` loops)  
![[Pasted image 20230814180516.png]]  

Functions are smaller blocks of code run individually.   
![[Pasted image 20230814180725.png]]  

The MCU has memory mapped peripherals which share the same address space as the register file and RAM. A specific address is used to access registers (memory) which control the peripheral, and contain the input/output data of the peripheral. This lets us write directly to memory for peripherals. The processor memory is sorted like:  
![[Pasted image 20230815003315.png]]  
32 Registers is used for temporary variables, e.g. Processor state  
64 I/O Registers is for mapped peripheral registers  
160 Ext I/O Registers also works along the 64 I/O Registers to provide easier use of peripherals by applying label names defining the addresses of these registers instead of us having to look them up in datasheet  
Internal SRAM is the RAM of the MCU, for code  

Header file `#include <avr/io.h>` is for definitions of various pre-defined label names for registers, peripherals, etc.  

### Ports:  
A GPIO can have 2 states: High (1) or low (0). When used as an output they produce a high or low output, when used as input they read either a high or low input.  

Internally, this is defined as either 1 or 0 binary. Externally, this is defined as MCU supply voltage (usually 5 v) or 0 v.  

The MCU has 23 GPIO pins spread across PORTB, PORTC, PORTD. 

Each GPIO port has 3 registers: DDRX, PORTX, and PINX, where X stands for the port label (e.g. DDRB).  
DDRX is the data direction register, PORTX is the data output register, PINX is the data input register.  

To set output of pin use the corresponding bit of the PORTX register (using shifting and masking).  
To read value of in use the corresponding bit of the PINX register where low voltage becomes 0 and high voltage becomes 1.  

DDRX register bits determine the type of the pin, and the PORTX/PINX register bits either output/read the bit on that pin. If DDRX pin is zero then it is an input pin be default, if DDRX pin is 1 then it becomes an output pin.  

Basically, DDRX register tells what the pin type is (read or output), PORTX is used to set the output value of the pin/set pullup resistors for input, PINX is used to read the input value of the pin.  

Input is set by default to prevent accidental voltage output to the circuit potentially causing short-circuit. It can also be thought of as a high impedance pin, i.e. Lets no current in. An output pin can be thought of as a voltage source.  

![[Pasted image 20230815025542.png]]  
This is an example of using button to generate input, when released the capacitor charges up causing a voltage drop across it, hence input becomes 1. When button is pressed it creates short circuit and discharges capacitor leaving input 0.  

Remember that pins are counted from the right. hence shifting provides easy way to activating pins, as left shift starts from the right.  

We can simplify bitwise operators in the same way as incrementing, i.e. `+=`, `|=`, etc.  

Example code:  
![[Pasted image 20230815030226.png]]  
Note we could also use register addresses directly instead, but is more complicated.  

To turn off remote optimization, go to Project, Properties, Toolchain, and under compiler tab go to optimization to set the level. This may help reduce storage use on the flash for code.  

***Lecture Mon 07 Aug has Proteus/Microchip studio workings***  

Basically,  
- OR mask will set values to 1 if mask bit is 1, and leave bits the same if mask bit is 0. Used to set a bit to 1 and leave everything else as is, using `x |= y`
- AND mask does nothing, mask values aren't the only factors (if original is zero then it remains zero regardless)
- NOT AND (~AND) will leave 0 as 0, and 1 as 1, and turn 1 into 0 if mask is 1 (remember inversed), used to set a bit to 0 and leave everything else as is, using `x &= ~(y)`

Right click and Add watch on a variable will allow viewing of variable in watch window (pops up automatically at bottom).  

### Communication:  
Simplex is one way, half-duplex is two way, full duplex is 2 one way (a receiver line and sender line).  

Synchronous transmission: Separate signal used to indicate start of each piece of data being transmitted, where the separate signal is usually the clock. Needs more channels but lower overhead (signal data) 
Asynchronous transmission: A signal 'sync' is also transmitted along data line so only one channel needed, but more data required.  

Serial transmission uses one line (advantage) but can only send one by one. Parallel transmission uses multiple lines (disadvantage) but can send more data simultaneously.  

A 'symbol' is data sent each time interval, in binary symbols are either 1 or 0.  

![[Pasted image 20230816010055.png]]  
UART is asynchronous, serial, full duplex.  

### UART:  
Used commonly everywhere including GPS. Data goes out of TX line and receives from RX line. TX of microntroller connects to RX of the external device. UART ahs 3 wires, TX, RX, and Ground (since voltage is used for the energy medium for transfer, ground is connected for both components). If simplex communications is used then only 2 are needed.  
Extensions to this protocol include flow control and synchronous transmission (which is USART).  

When transmitting data with UART, it takes 8-bit data and transmit each bit one at a time sequentially along TX-->RX line. Shift registers convert byte into individual bits for transfer, and the rightmost bit (least significant bit) is transmitted first.   
![[Pasted image 20230816012951.png]]

Each data byte transmitted starts with a 'start bit' which is a logic 0, it tells receiver to expect a transmission. Ending transmission with a 'stop bit' which is a logic 1 and tells receiver to stop receiving, and also ensures the receiver can tell the next start bit (since differing logic values).  

By default the line stays at logic 1 (not doing anything). An optional parity bit can be used before the stop bit to prevent corruption.  
![[Pasted image 20230816013314.png]]  
We can use multiple stop bits to ensure all data is transferred (receiver will maintain stop state longer so next input bit is not accidentally missed), however this means longer delay between transmissions.  

An example of UART wave:  
![[Pasted image 20230816013650.png]]  
A UART 'frame' or 'packet' consists of start bit, data bit(s), optional parity bit, and stop bit(s). Voltage level VCC = logic 1, voltage = logic 0. Note least significant bit (LSB) is transferred first from sender, so the packet byte is in reverse order (e.g. Bit 7 is actually the first bit in original byte, or LSB).   
![[Pasted image 20230816013857.png]]  
This forms a wave visually. The naming scheme of a byte is `<databits>N<stopbits> <parity type>`, e.g. "10N2 with odd parity" means 10 data bits, 2 stop bits, and an odd parity bit (1). 

The baud rate determines the time length of each bit. The time between each bit is inverse of baud rate, i.e. 
$$ Time\: per\: bit = \frac{1}{Baud\: rate}$$
Standard baud rates are 4800, 9600, 19200, etc. Not all baud rates are accepted by devices. 'Length' of a bit can be expressed as the time passed as the bit state as a wave, e.g. For bit = 0, the length would be the length of time the signal is at 0.  

Since each frame has some overhead (delay) to prevent signal loss, so the actual useful data sent over a frame is less than the actual amount of bits sent per frame. Since baud rate is rate of every bit, then:  
$$ Data \: rate = \frac{Data\:bits\:per\:frame}{Total\:bits\:per\:frame}*Baud\:rate $$
Essentially the ratio of useful data bits in each frame times baud rate. More parity/overhead bits means slower data rate.  

Transmission time is therefore data bits to transmit divided by data rate, i.e.  
![[Pasted image 20230816105016.png]]  

### USART specifications:  
The ATmega328P has 1 USART (Xplained Mini has 2) which has 1 data register and 4 control registers.  
USART0 is the only USART peripheral on MCU (on Xplained Mini it has 2 USARTs). Lectures refers it as UART0 as we use the asynchronous transmission. UART0 is associated with the DDRD pins.

UART0 has 5 registers:  
![[Pasted image 20230816122546.png]]  
Where UDR0 contains UART data, and the other 4 registers is to control the peripheral.
UDR0 contains RX and TX data. Outputting means we send to TX pin.    
![[Pasted image 20230816123038.png]]  

**UCSR0A:**  
Note: These registers control the UART.  
UCSR0A is the first control register that mainly contains flags. This is 8 bits and controls several things:  
![[Pasted image 20230816123139.png]]  
TXC0 checks if UART has sent bytes for transmission out to the receiver, it is set after fully transmitting a data frame. UDRE0 is set if UDR0 register (UART data register) is ready to receive data, although we aren't using UART receiving for project. Both flags can be used to check whether UART has finished transmitting. 

**UCSR0B:**  
UCSR0B mainly holds configurations, 8 bit.  
![[Pasted image 20230816125047.png]]  
TXEN0 enables the transmitting capabilities of UART, which we want (Simplex communication). UCSZ02 determines the byte size the UART can work with, which is 8 for our project (8N1 byte).  

**UCSR0C:**  
UCSR0C mainly holds important configurations, 8 bit:  
![[Pasted image 20230816125418.png]]  
UMSEL0 is a 2 bit setting (uses up 2 bits in UCSR0C register) determines the transmission type, i.e. Synchronous/asynchronous (we are using UART for project). UPM0 determines parity mode, not used. USBS0 is stop bit select, we use 1 bit. UCSZ0 is character size, we want 8 data bits. Note that we need UCSZ02 = 0 in UCRS0B to get character size = 0 (UCSZ02 configures character size but not directly).  

**UBRR0:**  
Baud rate register, 16 bit:  
![[Pasted image 20230816130242.png]]
UBRR0 is a 12 bit configuration (4 bits in UBRR0 is not used). Baud rate is defined by prescaling system clock to generate clock source for UART, where the prescaler value is determined by UBBR0\[12..0] bits.

More specifically, to calculate UBRR0,  
![[Pasted image 20230816144726.png]]  
The system clock will be divided by the value stored in UBRR0 (prescaler) and outputs that, in circuit output is foscn.  This output is passed through the dividers, to a total division of 16 (i.e. Output is divided by 16, 2\*4\*2). The final output is the actual baud rate derived from the UBRR0 register. The equation +1 because we start counting from 0 for UBRR0. f<sub>osc</sub> is frequency of system clock divided by prescaler (UBRR0).

Rearranging the baud rate equation gives the ideal value for UBRR0 register, it is not always a perfect integer so UBRR0 has to be an integer that can account for this.   

Example of setting UART:  
![[Pasted image 20230816150235.png]]  

### Transmitting:  
Setting the UDRE0 bit in UCSR0A register ensures byte is fully transmitted before sending another, usually done in a dedicated function   
![[Pasted image 20230816150431.png]]  
Send data byte to UDR0 register after confirmation of transmitting, while loop will keep running until it detects transmitting is complete.  

![[Pasted image 20230816151103.png]]  
Allows more data to be transmitted. Instead of sending one bit at a time we upload an array of bits, which represent a binary value, and each bit is transmitted one by one. Using `strlen` (needs `str.h`) lets us count the number of bits in an array, i.e. Amount of bits transmitted in a single transmission, for the loop needed to transmit all elements in the array.

We can send characters instead of number values through the UART via encoding. Common encodings include ASCII, Unicode, etc. ASCII table:  
![[Pasted image 20230816151347.png]]
Encoding essentially assigns certain bit combinations to other symbols that can be more easily interpreted by humans. 

Modulus operator can be useful to separate number characters from each other, e.g. `132 % 10` will give us the rightmost (least significant) digit, 2. To convert to ASCII, we add this value to the ASCII equivalent of zero, since ASCII is ordered sequentially. Since zero = 48 in ASCII, 2 + 48 = 50 = 2 in ASCII as well.  Integer division by ten can remove the ones leaving the others, e.g.  `132/10` is 13.2, since it's integer then .2 is removed leaving 13. Perform modulo again to get 3 (least significant bit) then repeat process again.  
![[Pasted image 20230816152118.png]]

UART can transmit string as long as the header file is included and variable is specified as string (use quotes).  
![[Pasted image 20230816152254.png]]  

Finally, for modular software:  
![[Pasted image 20230816152330.png]]  

UART IS COMMUNICATION PROTOCOL. The USART chip builds the foundation for this protocol and all we need to do is tell it what settings to use and what to send.  

In summary, to utilize the UART (note that the examples are poor examples of code writing):  
1. Configure the UART. This is a function that sets the registers of the UART configuration registers, i.e. UCSR0A, UCSR0B, UCSR0C, UBBR0.   ![[Pasted image 20230827210452.png]]
2. A function to load data byte to the UDR0 register, after checking the UDRE0 bit is set in UCSR0A register. ![[Pasted image 20230827210659.png]]
3. OPTIONAL: If we want to transmit multiple bytes we can write dedicated function to call the transmit function for each bit in array: ![[Pasted image 20230827210753.png]]
4. Finally, put it all together, along with `#include` files:  ![[Pasted image 20230827210839.png]]
Note that we use prototyping functions for readability, these define the functions but the actual functions are created somewhere else.  Also because the `uart_transmit_array` function accepts string and works with string, we don't need to convert the string to bits using ASCII before input, `\r` is carriage return signals end.  

Ideally, code should be modular and easily readable. This means:  
- Instead of writing all code in one `c` file (cluttered code) split it into multiple `c` files that can draw from each other into the main file
- Each code that relates to each peripheral should be contained in it's own `c` file, and their respective `h` files  
- Use `h` files for definitions in the code, and should be easily accessible to prevent confusion. These allow 'prototyping' of functions, defining functions but not creating them, which can be useful if multiple files need to use the same function to prevent name mix-ups

### ADC:  
Analog signals are continuous in time and amplitude. They are sensitive to noise, and often produced by nature.   
Digital signals are discrete in time and amplitude. They are less sensitive to noise, and cannot perfectly copy analog signals.  

Both type can be converted to each other via respective converters (Digital to Analog Converter DAC and Analog to Digital Converter ADC).  

Most of the time we want to sense/measure a physical property that isn't electricity. Electrical sensors convert a physical signal to electrical signal, and electrical actuators do the opposite (convert electrical to physical, e.g. Motor converts electricity to rotational).  

Analog signals contain lot of information which is good but means they are tricky to deal with and signal loss is easy which makes it harder to process. For most cases however digital signals will suffice.  

ADC conversion occurs by sampling the analogue signal at discrete time steps, called quantization. Based on the size of the time steps we can determine the signal loss during conversion.  
![[Pasted image 20230830004009.png]]  
(Rule of thumb: Discrete = countable by eye instead of equation). Basically, at each T time, note the amplitude of the analog signal and plot it. After one period we get a plot at each T time representing the amplitudes at that current moment, then we create a square signal based on the plotted points for a digital signal.  

Smaller time steps means less data loss but more bits required to hold this data, and hence more memory.  

Sampling time  = 1/sampling frequency/rate. Higher sampling rate means more accurate conversion but more data needed. To accurately capture a signal the sampling rate must be greater than the Nyquist frequency, which is equal to twice of the highest frequency in the signal.  

For increasing number of bits we can quantize greater range of values,  
![[Pasted image 20230830005044.png]]
Basically each bit represents a range of values from the analogue signal and maps it to a discrete fixed value, e.g. For 1 bit, 0 represents signals between 0v to 2.5v in the analogue signal. The entirety of the analogue signal from 0v to 2.5v is simplified to a 0 in digital signal, which means we lose a big range of data.  

Number of intervals = 2<sup>bits</sup>, where each interval represents a voltage range of the analogue signal. More bits = finer steps = more memory needed.  

However, the ADC converter always compares to a base reference voltage, e.g. 5v. This means if we have lesser steps we can exclude a signal entirely if the signal falls below a certain range. For example, if we have a 2v signal with 5v reference, with a 1 bit ADC since it is 0 from voltage range 0 to 2.5v then the 1 bit ADC will interpret the signal as 0 which is not true, hence signal loss. So interval steps are important to determine the range of values the ADC can detect and convert, e.g. For a signal that oscillates between 4.50v to 4.55v will need a lot of intervals in order to capture this.  

Acquisition time = How long it takes ADC to get sample of analog signal, including time taken for signals to propagate through circuit as well.  
Conversion time = How long it takes for ADC to convert analogue signal to digital signal.  
Total sampling time = Time taken to make a single ADC reading, i.e. Sum of acquisition and conversion time. The maximum sampling rate is limited by the minimum total sampling time, i.e.  
$$ f_{sample(max)} = \frac{1}{t_{acquisition(min)} + t_{conversion(min)}} $$
Resolution = Number of bits in ADC to represent a signal, i.e. Bits used for intervals  
Supply voltage (AV<sub>CC</sub>) = Voltage required to power ADC (5v for project)  
Reference voltage (V<sub>ref</sub>) = Determines maximum voltage range for ADC to convert signals, any signals that exceed reference voltage won't be converted  
Step size (V<sub>step</sub>) = Smallest signal that can be determined by ADC and is related to interval size, i.e.  
$$ V_{step} = \frac{V_{ref}}{2^{resolution}} $$
Different ADC's have different properties, e.g. Sampling rate, temperature stability, lower error, etc.  
The most common type include delta-sigma ADC, Successive Approximation Register (SAR) ADC, pipeline ADC.  

Microcontrollers typically use SAR ADC types, due to low part count, low power consumption, adjustable resolution.  

**For SAR ADCs:**    
In order to maintain a good steady input signal during quantization, we can 'capture' a signal waveform and hold it until quantization is finished. The sampling process does this by storing a sample of the signal, which is done via circuitry, for example, utilizing switch and capacitor.   
![[Pasted image 20230830194319.png]]  
When the switch is closed the capacitor will charge up, the rate it charges up is based on time constant (= RC) which determines the minimum time to get a stable sample (fully charged). Then when the switch is opened the capacitor retains the charge for a while, and this is where the sampling process occurs before capacitor discharges. Then switch is closed again, process repeats. 

Maximum ADC clock is then the safe speed that we can close/open the switch to get stable samples, any faster and we get bad samples. Inversely it is also true that we need a minimum clock frequency to prevent the capacitor discharging too early, so minimum clock frequency also exists. 

SAR conversion can be expressed in graph form or table form.   
![[Pasted image 20230831131914.png]]  
In graph form, We take half of the reference voltage and compare it with the input voltage (this is one bit). If the input is higher than it becomes a 1, if it is lower it becomes a 0. We can further improve the accuracy of the conversion by adding additional bits. For each additional bit, we take half of the difference between the previous reference in the direction of the weight, i.e. If it was 1, then we go higher, if it was 0 then we go lower. Basically for each additional bit half out reference and go either higher or lower depending on previous result. More bits mean better accuracy.  

In tabular form,  
![[Pasted image 20230831135409.png]]  
Instead we represent the intervals as bit values, for an 8 bit ADC the maximum value is 256 so we get 256 intervals. Hence, based on the reference voltage, each interval is 2.56/256 = 0.1V. Then we compare and weight the input signal like the graph form, where we set a upper, lower, and middle value. The upper value starts at the maximum reference voltage, and only goes down if the input signal is less than the middle value. The lower value is the previous middle value, and middle is halfway between upper and lower. Bit is 1 if input is higher than middle, 0 if less than middle. Note that each clock cycle represents one conversion for one bit.  

The switch is responsible for obtaining the 'points' from the input signal, which plots an approximation of the input signal as discrete values rather than an analogue signal. The successive approximation is what converts these points into a digital byte. The whole system is held inside the ADC, but the switch circuit can also be built outside of the ADC. 

**ADC channels:**  
Instead of having multiple ADCs for converting multiple signals we can use a single ADC and multiplexer. Each input is referred to as a ADC channel, and these inputs are controlled via channel selection input  
![[Pasted image 20230901003023.png]]  
So instead of simultaneously measuring volage and current it alternates between voltage and current signals. This also means that voltage and current readings won't originate at the same time position.  

### ADC registers:  
For the ATmega328p, it has one ADC, which contains 8 ADC channels (pins). There are 5 registers associated with the ADC.  
![[Pasted image 20230901163830.png]]  
ADMUX controls the selection of the multiplexer that switches the channel inputs, ADCH and ADCL store the conversion result. The other 3 registers control the peripheral, i.e. Configuration. Note that for the config registers some fields (register bits) can be set manually and others are set by ADC.

**ADMUX register:**    
![[Pasted image 20230901164121.png]]  
REFS\[1..0] is the reference selection where 00 = AREF, 01 = AVCC, 10 = Reserved, 11 = Internal 1.1v. This determines the value of the reference voltage, for the project AVCC will set the reference to the VCC voltage of 5v.    
ADLAR is left adjust result (?)  
MUX\[3..0] determines the pin input, 4 bits means it can hold 16 different values.  
![[Pasted image 20230901164449.png]]  
Basically ADMUX determines reference values for ADC.

**ADCSRA register:**  
![[Pasted image 20230901185802.png]]  
![[Pasted image 20230901185809.png]]  
- ADEN turns on ADC  
- ADSC initiates a conversion by reading the input at the activated channel and triggers the ADIF flag bit once sample is taken and converted  
- ADATE enables auto trigger mode which initiates conversion as soon as the current sample is finished converting.  
- ADIF is the interrupt flag that is set after completing a conversion to indicate conversion finish, and cleared when executing an interrupt
- ADIE allows the ADC to generate an ISR (interrupt service routine) after conversion  
- ADPS\[2..0] sets the prescaler which the system clock is divided by to fit the clock requirements of the ADC. Since system clock can't be altered we can instead scale it down for ADC clock.  

**ADCSRB register:**  
![[Pasted image 20230902233745.png]]  
When auto trigger is set we can do things with it, such as set interrupts with ADTS\[2..0] bits.  

**DIDRO register:**   
![[Pasted image 20230903000957.png]]  
Is optional.  

**ADCL and ADCH registers:**  
![[Pasted image 20230903003159.png]]  
Contains 16 bits overall spread across two 8bit registers, which contains the converted signal.  

The ADC timing diagram further explains clock usage:  
![[Pasted image 20230904002400.png]]  
The ADC will take 1.5 cycles to sample, and for the remaining 11.5 cycles it will conduct SAR conversion (i.e. Compare input with half values of reference, and repeat for as many bits given). Since we have 10 bits, then minimum of 10 cycles required to fully convert (additional cycles is for writing data). In total, 13 cycles of ADC clock to conduct 1 conversion. However, with auto trigger mode, additional 0.5 cycles needed, so total of 13.5 cycles in auto trigger mode.  

Note that when turning on the ADC it needs time to setup, cycles needed is in datasheet.  

Total time taken is the number of cycles divided by ADC clock frequency.   

Example code to configure ADC:  
![[Pasted image 20230904010025.png]]  
We set ADCSRA settings, ADCSRB and DIDR0 are all set to zero. Note that we can simply shift via register names rather than using binary values, e.g. `ADCSRA |= (1<<ADEN)`, where ADEN is the 7th bit in `ADCSRA` register, hence it shifts the 1 by 7 positions.  

Performing a conversion:  
![[Pasted image 20230904213207.png]]  
Using a `while` loop we can wait until the ADIF bit, which sets the conversion flag, is equal to 1. Since C runs line by line then the `while` loop will occupy the code until loop is broken. This is an example of polling rather that using interrupts.  

Combining code:  
![[Pasted image 20230904231031.png]]  
ADC converted value (`uint32_t`) is simply read by passing it. Note the value is multiplied by 5000 (millivolts, since volts gives decimals) and divided by 1024 (conversions steps). The `printf` function is a custom function for transmitting data through UART (not provided). The '2' is the channel of ADC used.  

**Non-ideal ADCs:**
While previous example was considering an ideal ADC in reality ADC have errors. The absolute accuracy is the sum of the error, measured in least significant bits (LSB) and is typically one step size.  
![[Pasted image 20230905011934.png]]  
V<sub>step</sub> is the step voltage, which is V<sub>ref</sub>/2<sup>bits</sup>, and gives the +/- range of the error in voltage.  

### Timers:  
All microcontrollers can 'sense' time via their system clock, and each clock period is a 1/clock frequency.  
Timers are peripherals that convert system clock periods (T<sub>system_clk</sub>) into actions in real time or measure events in real time. 

The microcontroller processor also can 'sense' time via CPU clock, same as the system clock in microcontroller. It's possible to create a timer in software by writing 'dummy' code that does nothing except taking up execution cycles to delay program time, and hence acts as a time delay. But this is inefficient and stops the whole program during delay.  

The `NOP` operation in assembly creates a single execution cycle delay. Using `asm("NOP")` in C allows us to utilize this operation in C code, and this code can be repeated many times. However this operation still has the same problem of delaying the whole program which prevents it from doing anything else during delay, but is suitable for very small clock delays.  

The timer peripheral on ATmega328P can also be used for timers. It works by using a counter that up/down when the input changes. If counting up, then count is increased every time the input changes from low to high, and if counting down, the count is decreased every time the input changes from low to high. The input is usually a clock, either the system clock or a prescaler.  
![[Pasted image 20230911112857.png]]  
Since we generally use 8 bits, then typically once the count exceeds 255 then it will reset to 0 at the next increment at 255. For the ATmega328P we can also set it to reset at a certain value instead (TOP), instead of the maximum value (MAX).  
![[Pasted image 20230911113011.png]]  
When timer resets, also called overflow, it generates an event/flag that can be detected and used for specific timings.  

We can also compare instead, setting a value to compare with the current timer value. When they match then compare match occurs which sets an event/flag as well that can be used to detect timings.  

Overflow and compare match events can be used to generate a pulse width modulated (PWM) signal.  

An external clock can also be used instead of the system clock to increment/decrement the counter, but the timer is still bounded to the system clock, hence it will only increment/decrement if the system clock is high  
![[Pasted image 20230911113540.png]]  

The prescaler allows us to use a wider range of clock frequencies as we can scale them if they are too low/high. The timer clock is created by the system clock frequency divided by the prescaler, i.e.  
![[Pasted image 20230911114100.png]]  

The number of bits allocated to the count register is the full range of values it can hold based on the number of bits, i.e. 0 to 2<sup>N</sup>  

Resolution is the minimum time interval the timer can measure and is equal to one timer period,  
![[Pasted image 20230911114256.png]]  
Basically the smallest time interval that the timer can count by, e.g. If resolution is 2ms then timer cannot count 1ms.

Range is the maximum time interval the timer can measure, i.e. The maximum count before overflow,   
![[Pasted image 20230911114452.png]]  

TOP is the count value at which the count will reset, and must be less or equal to the maximum possible count value stored in available bits.  

Period is the time interval taken for the count to return to the starting value,   
![[Pasted image 20230911114706.png]]  
To get a desired period rearrange for TOP, which goes in OCR0A register.

**Timer peripherals:**  
The ATmega328P has 3 timer peripherals (Timer0, Timer1, Timer2). Timer0 is sufficient of this project.  

In the ATmega328P there are 3 pins associated with Timer/counter0 (TC0): PD4, PD5, PD6.  
- PD4 is T0 and provides external clock source  
- PD5/PD6 is OC0B/OC0A and both are used to generate signals based on compare match events  

There are 7 registers in TC0:  
![[Pasted image 20230911120720.png]]  
- TCCR0A and TCCR0B are used to configure TC0 peripheral  
- TCNT0 is an 8 bit register that holds the current count value
- OCR0A and OCR0B are used to setup the compare match value, and in some modes can setup the TOP
- TIMSK0 is used to configure interrupts 
- TIFR0 contains flags  

**TCCR0A register:**  
![[Pasted image 20230911120957.png]]  
COM0A and COM0B do the same thing but output on different pins, they are used to determine the compare match output. If the timer matches the value in register then the compare match flag occurs, and the event that happens depends on the settings set by COM0A and COM0B which output to different pins. For example, if COM0A is on 11, then for each match the output pin is set as high. Waveform generation is for configuring counter mechanism, e.g. Count until TOP instead of max (note this only raises compare match flag and not overflow flag). 

**TCCR0B register:**  
![[Pasted image 20230911121442.png]]  
Note that WGM02 bits exist in TCCR0B register, so in order to utilize waveform generator mode settings both bits from registers are needed (WGM0\[1..0] and WGM0\[2]). FOC0A and FOC0B forces a compare match flag, typically unused. CS0\[2..0] bits is for prescaler, timer will run automatically unless 000 is set. 

**TCNT0 register:**  
![[Pasted image 20230911121456.png]]  
Register stores the current value of timer. Can be used to store current time and compare times. 

**OCR0A/OCR0B registers:**  
![[Pasted image 20230911121522.png]]  
Set the TOP values for comparison for timer. These registers set the value to be matched with the timer and what triggers the compare match event. 

**TIMSK0 register:**  
![[Pasted image 20230911121536.png]]  
Determines interrupts and enables them, used when compare match event occurs.

**TIFR0 register:**  
![[Pasted image 20230911121553.png]]  
For interrupt flags. Bits tell the state of interrupt flag, e.g. If TOV0 = 1 then overflow has occurred. We can read these bits for handling events. If we don't care about the flag we can leave it as 1, and only reset when we handle the event so it can be triggered again. 

**PWM:**  
Pulse width modulation (PWM) can be generated with timers. It is a on/off signal that alternates between high and low, and the time period of the signal can be controlled via timer flags. 
![[Pasted image 20230915124300.png]]  
PWM allows us to output a non-discrete value from microcontroller which only deals with high/low outputs. By controlling the amount of time the signal is high in the period, the overall output is interpreted similarly to RMS in AC signals, where the average of the signal output is controllable and non-discrete. For example, if microcontroller can only output 0v or 5v, then having 50% duty cycle (50% of signal is high) we can achieve average signal of 2.5v.  

Duty cycle is T<sub>on</sub>/T<sub>p</sub>, essentially the percentage of time on vs overall time period. The average value of the output signal is duty cycle times the high voltage (i.e. Max voltage output).  

Passing a PWM signal through a low-pass filter can produce DC signal with average value.   
![[Pasted image 20230915124813.png]]  
	
A timer can be used to generate PWM signal, as we can set the compare value to reset the timer, hence we can control the amount of time before reset, and we can bind this event to produce high outputs at periodic intervals. We need to set the appropriate timer registers to PWM mode(s), which doesn't reset on compare match, instead it resets on TOP value. This maintains frequency of timer which is important for PWM to maintain steady signal. For example, the output pin is high when timer reaches compare match, and goes to low when timer resets (due to hitting TOP). Note that the compare match DOES affect the output, but does NOT reset the timer.  
![[Pasted image 20230915125449.png]]  
Example code:  
![[Pasted image 20230915125648.png]]  

### Interrupts:  
Polling method for dealing with events is to essentially wait until receiving the event, but this usually delays the rest of the microcontroller and prevents it from doing anything else, which is inefficient. Polling is easier to do and doesn't need additional hardware, but takes longer and inefficient.  

Interrupts can deal with this, they wait for an event and should the event occur it will stop normal program execution, run a specific function, then return back to where the program was before.  

Interrupts can respond almost immediately, and has priority so events are handled first. However extra hardware needed, state of processor is not known during interrupt, code and memory is more complex.  

Interrupts are not necessarily better than polling depending on the situation. Interrupts should be used when the event is asynchronous (unknown when event will occur), urgent (needs immediate response), infrequent (doesn't happen a lot).  

An Interrupt Service Routine (ISR) is a special function run during an interrupt. ISR is a function with no arguments and returns (in general). The only way for an ISR to communicate with the rest of the code is through global variables. Each interrupt type has its own ISR which are executed based on priority, and ISRs are not called as part of normal program execution.  

![[Pasted image 20230913112910.png]]  

We use global variables to allow ISRs to change things in the program, which means these variables will change anytime during runtime. `volatile` is required to tell the system that this variable will change during runtime, otherwise it is usually optimized to a fixed value.  

![[Pasted image 20230913113657.png]]  

The microcontroller has specific hardware lines to signal interrupts. Interrupt vectors are addresses of ISRs stored in system memory, and can be accessed with interrupt vector table.   

When an interrupt occurs it completes the current instruction, then stores the address of the next instruction in stack memory during ISR. The ISR address of the interrupt is loaded by the processor to the program counter and ISR execution occurs. When ISR is finished, address of the next instruction is loaded from memory stack to the program counter, then program execution continues from that address. If any other interrupts occurs during ISR execution then those are loaded up instead based on priority.  

The ATmega328P supports multiple interrupts including GPIO level changes, UART receive complete, ADC conversion completion, etc.  

Each interrupt is disabled by default, so needs to be turned on to use it. Global interrupt bit is also off by default so needs to be set on to enable interrupts. Global interrupts are also automatically disabled when an interrupt occurs and reenabled when finishing an ISR. It takes a minimum of 4 cycles to execute ISR address from interrupt vector table.  

External interrupt pins INT0 and INT1 on ATmega328P are PD2 and PD3. Any of the pin change interrupts (PCINTx) pins can also be used as interrupt sources but they share the same ISR.  

The SREG register holds the global enable bit for interrupts. Interrupts associated with a peripheral are controller by bits in the peripheral's registers. Each interrupt usually has 2 bits involved: Setting interrupt enable bit, which causes an interrupt to be triggered by an interrupt event, and interrupt flag bit, which is set whenever an interrupt event occurs regardless of whether the interrupt enable bit is on or not.  

A flag bit is used as an indicator for the status of interrupt. The interrupt flag bit is cleared automatically when the ISR for that interrupt is executed, or it can be cleared manually by writing 1 to the bit.  

**SREG register:**  
![[Pasted image 20230913120846.png]]  
![[Pasted image 20230913120854.png]]

Peripherals have their own registers containing interrupt bits,  
![[Pasted image 20230913121202.png]]  

Example: Setting timer interrupt:  
![[Pasted image 20230913121507.png]]  
![[Pasted image 20230913121517.png]]  
Needs `avr/interrupt.h` for interrupt vector macros, in this case `TIMER0_COMPA_vect` is interrupt vector macro.   
![[Pasted image 20230913121735.png]]  
`sei()` enables global interrupts at the end of ISR.  

ISRs should have no loops and be short and quick. Ideally ISRs should be used to simply indicate the even and the actual code to handle the event is run in the main program.  

### Memory:  
RAM is split into three sections: 
- Stack: Used for temporary storage of variables associated with functions  
- Heap: Used for storing dynamic variables, set to a fixed size by programmer
- Data segment: Used for storage of static/global variables that exceed function scope, set to a fixed size depending on how many of these variables need to be stored.  
![[Pasted image 20230913123035.png]]
The combination of stack, heap, and data segment cannot exceed RAM size. Doing so is called stack overflow/collision.  

High stack usage is mainly due to recursive functions or large arrays in functions  
High heap usage is mainly due to using `malloc()` to create large dynamic arrays or not releasing allocated memory using `free()`  
High data usage is mainly due to allocating large arrays with static/global scope  

**Stack:**  
The stack is a data block that stores local variables, function parameters, return values, return addresses for functions and ISRs, temporary storage of register values.  

Usually stack starts at the last RAM address (highest) and grows down.  
![[Pasted image 20230913124736.png]]  
The stack operates on the last in, first out (LIFO) buffer. The stack pointer stores the address of the next available location in the stack. Stack pointer is decremented each time data is pushed into stack, and incremented when data is popped out of stack.  
![[Pasted image 20230913124903.png]]  
To add data to stack it goes in the pointer address, then pointer is decremented to lower address. To remove data pointer is incremented to upper address, then removes data at pointer.  

RAM example:  
![[Pasted image 20230913125104.png]]  




### General microchip stuff:  
Important includes are `<avr/io.h>`, `<stdint.h>`, `<string.h>`. Note for user `h` files, the notation is `#include "asdasd.h"`. `#include <avr/portpins.h>` somehow allows usage of PB5, PC3, etc macros.

To test program with Proteus, build the program in Microchip Studio to compile it, then go to Proteus project that has a ATmega328P component on it. Edit properties on the ATmega328P, select the .elf file of the built microchip project as a program file. Set clock frequency as needed, and external clock as 0000. Use run simulation tab to simulate program, virtual terminal can be used to produce an output.  

To use puTTy with microchip, use the micro USB cable from to connect to microchip. Open puTTy and set baud rate and clock frequency. To find serial port go to device manager and look at serial connections.

Strings in C are automatically stored as bytes, so doesn't need conversion to ASCII, and simply uses "". We can use either \[] (in variable name) or \* (after type declaration) to form strings, which are `char` arrays in C. 
Using `char* <varname> = "<text>"` denotes a pointer to the string, which means we can do `<varname> = "<newtext>"` which is valid, but cannot do `<varname[0] = 4`, or edit the elements in the string unless we override it with another string. 
Using `char <varname>[] = "<text>"` forms a char array, so we can use typical array operations on the string such as `<varname>[0] = 4` but cannot edit the whole string without using a loop. 
Also remember that strings in C have `\0` at the end as a ending reference.  

Note that because a pointer is essentially an integer value, we can increment/decrement it. In an array, incrementing/decrementing a pointer will move it along the elements of the array instead, as the elements of an array are typically placed next to each other in memory.  








