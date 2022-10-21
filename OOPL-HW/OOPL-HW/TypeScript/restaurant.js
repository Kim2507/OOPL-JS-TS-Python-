var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var Restaurant = /** @class */ (function () {
    function Restaurant(name, city) {
        this.name = name;
        this.city = city;
    }
    return Restaurant;
}());
var IceCreamStand = /** @class */ (function (_super) {
    __extends(IceCreamStand, _super);
    function IceCreamStand(name, city, flavors) {
        var _this = _super.call(this, name, city) || this;
        _this.flavors = flavors;
        return _this;
    }
    return IceCreamStand;
}(Restaurant));
var flavors = ["Vani", "Chocolate", "Mint"];
var icecream = new IceCreamStand("J&J", "Boston", flavors);
console.log(icecream);
