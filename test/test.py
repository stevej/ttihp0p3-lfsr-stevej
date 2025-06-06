# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 3)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # Wait for one clock cycle to see the output values
    await ClockCycles(dut.clk, 1)

    numbers = []
    for i in range(20):
        number = int(dut.uo_out.value)
        numbers.append(number)
        await ClockCycles(dut.clk, 1)

    unique_numbers = sorted(set(numbers))

    # Few duplicates were found
    assert len(unique_numbers) > 17




@cocotb.test()
async def test_seed(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 3)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # Wait for one clock cycle to see the output values
    await ClockCycles(dut.clk, 1)

    dut.ui_in.value = 0x50
    dut.uio_in.value = 0b1000_0000

    await ClockCycles(dut.clk, 1)
    numbers = []
    for i in range(20):
        number = int(dut.uo_out.value)
        #print(number)
        numbers.append(number)
        await ClockCycles(dut.clk, 1)

    unique_numbers = sorted(set(numbers))

    # Few duplicates were found
    assert len(unique_numbers) > 17

    # Keep testing the module by changing the input values, waiting for
    # one or more clock cycles, and asserting the expected output values.

