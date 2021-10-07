// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.5.1;
//pragma solidity >=0.7.0 <0.9.0;


contract smart_contract {
   
    string public constant value = "default_value"; 
    
    // enum data struct to enumerate state available
    enum State { Waiting, Ready, Active }
    State public state;
    
    // set the default status
    constructor() public {
        state = State.Waiting;
    }

    // activation function
    function activate() public {
        state = State.Active;
    }
    
    // check status
    function is_active() public view returns(bool) {
        return state == State.Active;
    }
    
}
