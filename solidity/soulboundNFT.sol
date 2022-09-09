// SPDX-License-Identifier: MIT
// Soulbound NFT Test (from lorenzozaccagnini.it)

pragma solidity ^0.8.13;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTToken is ERC721, Ownable {
using Counters for Counters.Counter;

    Counters.Counter private _tokenIdCounter;

    constructor() ERC721("Soulbound", "SBNFT") {}

    modifier oneTransfer(address from) {
        require(
            from == 0x0000000000000000000000000000000000000000,
            "Soulbound nft can't be transferred"
        );
        _;
    }

    function safeMint(address to) public onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override oneTransfer(from) {
        super._beforeTokenTransfer(from, to, tokenId);
    }

}
