/*
* meal.js
* */
var app = getApp();
Page({
    onLoad:function () {
        wx.setNavigationBarTitle({
            title:app.globalData.shopName
        })
    }
});