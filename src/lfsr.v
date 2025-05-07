`ifndef _LFSR_
`define _LFSR_

module lfsr (
    input logic clk,
    input logic rst_n,
    input logic write_enable,  // Set the seed
    input logic [7:0] seed,
    output logic [7:0] lfsr_bits
);

  reg [7:0] r_lfsr;
  reg r_xnor;

  assign lfsr_bits = r_lfsr;

  always_ff @(posedge clk) begin
    if (!rst_n) begin
      r_lfsr <= '1;
      r_xnor <= '0;
    end else begin
      // On write_enable, load the lfsr with the given seed.
      if (write_enable) begin
        r_lfsr <= seed;
      end else begin
        r_lfsr <= {r_lfsr[6:0], r_xnor};
        r_xnor <= r_lfsr[7] ^ r_lfsr[6];
      end
    end
  end

endmodule
`endif
