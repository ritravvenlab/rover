--Copyright 1986-2017 Xilinx, Inc. All Rights Reserved.
----------------------------------------------------------------------------------
--Tool Version: Vivado v.2017.2 (win64) Build 1909853 Thu Jun 15 18:39:09 MDT 2017
--Date        : Mon Apr  9 09:04:02 2018
--Host        : jerome running 64-bit Service Pack 1  (build 7601)
--Command     : generate_target receiver_wrapper.bd
--Design      : receiver_wrapper
--Purpose     : IP block netlist
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity receiver_wrapper is
  port (
    S00_AXI1_araddr : in STD_LOGIC_VECTOR ( 5 downto 0 );
    S00_AXI1_arprot : in STD_LOGIC_VECTOR ( 2 downto 0 );
    S00_AXI1_arready : out STD_LOGIC;
    S00_AXI1_arvalid : in STD_LOGIC;
    S00_AXI1_awaddr : in STD_LOGIC_VECTOR ( 5 downto 0 );
    S00_AXI1_awprot : in STD_LOGIC_VECTOR ( 2 downto 0 );
    S00_AXI1_awready : out STD_LOGIC;
    S00_AXI1_awvalid : in STD_LOGIC;
    S00_AXI1_bready : in STD_LOGIC;
    S00_AXI1_bresp : out STD_LOGIC_VECTOR ( 1 downto 0 );
    S00_AXI1_bvalid : out STD_LOGIC;
    S00_AXI1_rdata : out STD_LOGIC_VECTOR ( 31 downto 0 );
    S00_AXI1_rready : in STD_LOGIC;
    S00_AXI1_rresp : out STD_LOGIC_VECTOR ( 1 downto 0 );
    S00_AXI1_rvalid : out STD_LOGIC;
    S00_AXI1_wdata : in STD_LOGIC_VECTOR ( 31 downto 0 );
    S00_AXI1_wready : out STD_LOGIC;
    S00_AXI1_wstrb : in STD_LOGIC_VECTOR ( 3 downto 0 );
    S00_AXI1_wvalid : in STD_LOGIC;
    clk : in STD_LOGIC;
    reset_n : in STD_LOGIC_VECTOR ( 0 to 0 );
    rx : in STD_LOGIC
  );
end receiver_wrapper;

architecture STRUCTURE of receiver_wrapper is
  component receiver is
  port (
    clk : in STD_LOGIC;
    rx : in STD_LOGIC;
    reset_n : in STD_LOGIC_VECTOR ( 0 to 0 );
    S00_AXI1_awaddr : in STD_LOGIC_VECTOR ( 5 downto 0 );
    S00_AXI1_awprot : in STD_LOGIC_VECTOR ( 2 downto 0 );
    S00_AXI1_awvalid : in STD_LOGIC;
    S00_AXI1_awready : out STD_LOGIC;
    S00_AXI1_wdata : in STD_LOGIC_VECTOR ( 31 downto 0 );
    S00_AXI1_wstrb : in STD_LOGIC_VECTOR ( 3 downto 0 );
    S00_AXI1_wvalid : in STD_LOGIC;
    S00_AXI1_wready : out STD_LOGIC;
    S00_AXI1_bresp : out STD_LOGIC_VECTOR ( 1 downto 0 );
    S00_AXI1_bvalid : out STD_LOGIC;
    S00_AXI1_bready : in STD_LOGIC;
    S00_AXI1_araddr : in STD_LOGIC_VECTOR ( 5 downto 0 );
    S00_AXI1_arprot : in STD_LOGIC_VECTOR ( 2 downto 0 );
    S00_AXI1_arvalid : in STD_LOGIC;
    S00_AXI1_arready : out STD_LOGIC;
    S00_AXI1_rdata : out STD_LOGIC_VECTOR ( 31 downto 0 );
    S00_AXI1_rresp : out STD_LOGIC_VECTOR ( 1 downto 0 );
    S00_AXI1_rvalid : out STD_LOGIC;
    S00_AXI1_rready : in STD_LOGIC
  );
  end component receiver;
begin
receiver_i: component receiver
     port map (
      S00_AXI1_araddr(5 downto 0) => S00_AXI1_araddr(5 downto 0),
      S00_AXI1_arprot(2 downto 0) => S00_AXI1_arprot(2 downto 0),
      S00_AXI1_arready => S00_AXI1_arready,
      S00_AXI1_arvalid => S00_AXI1_arvalid,
      S00_AXI1_awaddr(5 downto 0) => S00_AXI1_awaddr(5 downto 0),
      S00_AXI1_awprot(2 downto 0) => S00_AXI1_awprot(2 downto 0),
      S00_AXI1_awready => S00_AXI1_awready,
      S00_AXI1_awvalid => S00_AXI1_awvalid,
      S00_AXI1_bready => S00_AXI1_bready,
      S00_AXI1_bresp(1 downto 0) => S00_AXI1_bresp(1 downto 0),
      S00_AXI1_bvalid => S00_AXI1_bvalid,
      S00_AXI1_rdata(31 downto 0) => S00_AXI1_rdata(31 downto 0),
      S00_AXI1_rready => S00_AXI1_rready,
      S00_AXI1_rresp(1 downto 0) => S00_AXI1_rresp(1 downto 0),
      S00_AXI1_rvalid => S00_AXI1_rvalid,
      S00_AXI1_wdata(31 downto 0) => S00_AXI1_wdata(31 downto 0),
      S00_AXI1_wready => S00_AXI1_wready,
      S00_AXI1_wstrb(3 downto 0) => S00_AXI1_wstrb(3 downto 0),
      S00_AXI1_wvalid => S00_AXI1_wvalid,
      clk => clk,
      reset_n(0) => reset_n(0),
      rx => rx
    );
end STRUCTURE;
