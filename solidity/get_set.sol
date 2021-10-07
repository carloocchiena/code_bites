// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.5.1;
//pragma solidity >=0.7.0 <0.9.0;


contract smart_contract {
    string value; // state variable written to storage 
    
    // define get function to access variable
    // public = anyone on the blockchain can see it; external is more GAS efficient but check pragma 
    //memory tells solidity to create a chunk of space for the variable at method runtime, guaranteeing its size and structure for future use in that method.

//memory cannot be used at the contract level. Only in methods.
    // returns = specify the return type (see: value type)
    function get() public view returns(string memory) {
        return value;
    }
    
    // define set function to set value of our variable "value"
    // it's again a public\external function 
    // just defined a local "_value" variable for configuration purpose
    function set(string memory _value) public {
        value = _value;
    }
    
    
    // define a constructor with a default value
    // again, publicily accessible, this is mandatory for constructor
    constructor() public {
        value = "default_value";
    }

    
    
}






