/**
 * \file Cpu0_Main.c
 * \brief Main function definition for Cpu core 0 .
 *
 * \copyright Copyright (c) 2015 Infineon Technologies AG. All rights reserved.
 *
 *
 *
 *                                 IMPORTANT NOTICE
 *
 *
 * Infineon Technologies AG (Infineon) is supplying this file for use
 * exclusively with Infineon's microcontroller products. This file can be freely
 * distributed within development tools that are supporting such microcontroller
 * products.
 *
 * THIS SOFTWARE IS PROVIDED "AS IS".  NO WARRANTIES, WHETHER EXPRESS, IMPLIED
 * OR STATUTORY, INCLUDING, BUT NOT LIMITED TO, IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE APPLY TO THIS SOFTWARE.
 * INFINEON SHALL NOT, IN ANY CIRCUMSTANCES, BE LIABLE FOR SPECIAL, INCIDENTAL,
 * OR CONSEQUENTIAL DAMAGES, FOR ANY REASON WHATSOEVER.
 *
 */

#include "Ifx_Types.h"
#include "IfxCpu.h"
#include "IfxScuWdt.h"
#include "Ifx_reg.h"

#define GPT120_INT 12


int core0_main (void)
{
	IfxCpu_enableInterrupts();
    /*
     * !!WATCHDOG0 AND SAFETY WATCHDOG ARE DISABLED HERE!!
     * Enable the watchdog in the demo if it is required and also service the watchdog periodically
     * */

    IfxScuWdt_disableCpuWatchdog (IfxScuWdt_getCpuWatchdogPassword ());
    IfxScuWdt_disableSafetyWatchdog (IfxScuWdt_getSafetyWatchdogPassword ());
    IfxScuWdt_clearCpuEndinit(IfxScuWdt_getCpuWatchdogPassword ());
    GPT120_CLC.B.DISR = 0;
        IfxScuWdt_setCpuEndinit(IfxScuWdt_getCpuWatchdogPassword ());

        GPT120_CAPREL.B.CAPREL = 25000;

        GPT120_T6CON.B.T6UD = 1;
        GPT120_T6CON.B.T6UD = 1;

        SRC_GPT120T6.B.SRPN = GPT120_INT;
        SRC_GPT120T6.B.TOS = 0;
        SRC_GPT120T6.B.SRE = 1;

        P33_IOCR0.U = 0x80808080;
        P33_IOCR4.U = 0x80808080;
        P13_IOCR0.U = 0x80808080;
        P13_OMR.U = ((1<<4)-1);
        P33_OUT.U = 0x03C;
       // P13_OUT.U = 0xE;
        GPT120_T6CON.B.T6R = 1;



    while (1)
    {

    }
    return (1);
}

unsigned int counter=0;

IFX_INTERRUPT(Gpt_Isr, 0, GPT120_INT)
{
	counter++;

	if(counter==1500 )
	{
		P33_OUT.U = 0x03E;
		P13_OUT.U = 0xE;
	}
	if(counter==3000)
	{
		P33_OUT.U = 0x07C;

	}

	if(counter ==4500)
	{
		P33_OUT.U = 0x03C;
		counter=0;
	}
	}
