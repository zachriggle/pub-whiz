Ember.ENV.EXPERIMENTAL_CONTROL_HELPER = true;
Ember.LOG_BINDINGS = true;
Ember.ENV.RAISE_ON_DEPRECATION = true
Ember.LOG_STACKTRACE_ON_DEPRECATION = true

window.App = Ember.Application.create({
    rootElement: '#app',
    LOG_TRANSITIONS: true
});

App.Router.map(function() {
  this.resource('bars', function() {
      this.resource('bar', {path:':bar_id'});
  });
});

App.IndexRoute = Ember.Route.extend({
    redirect: function() {
        this.transitionTo('bars'); 
    }
});

App.ApplicationRoute = Ember.Route.extend({
});

App.BarsRoute = Ember.Route.extend({
    model: function() {
        return App.Bar.find();
    }
});

App.BarRoute = Ember.Route.extend({
    model: function(params) {
        return App.Bar.find(params.bar_id);
    }
});

App.BarsController = Ember.ArrayController.extend();

App.BarController = Ember.ObjectController.extend({
  sortedBeers: (function () {
    return Ember.ArrayProxy.createWithMixins(Ember.SortableMixin, {
      sortProperties: ['score'],
      content: this.get('content.beers'),
      sortAscending: false
    })
  }).property('content.beers')
})


App.Store = DS.Store.extend({
      revision: 12,
      adapter: DS.FixtureAdapter.create()
});

App.Beer = DS.Model.extend({
  name:  DS.attr('string'),
  score: DS.attr('number'),
  url:   DS.attr('string'),
  bar:  DS.belongsTo('App.Bar')
});

App.Bar = DS.Model.extend({
  name: DS.attr('string'),
  description: DS.attr('string'),
  details: DS.attr('string'),
  beers: DS.hasMany('App.Beer'),
  url:   DS.attr('string'),
  map:   DS.attr('string')
});

// App.Beer.FIXTURES = [{
//   id: 1,
//   name: "Pliny the Younger",
//   score: 100,
//   url: "#",
//   bar: 1
// }, {
//   id: 2,
//   name: "Pliny the Elder",
//   score: 20,
//   url: "#",
//   bar: 1
// }, {
//   id: 3,
//   name: "Hopslam",
//   score: 30,
//   url: "#"
// }, {
//   id: 4,
//   name: "KBS",
//   score: 97,
//   url: "http://google.com"
// }, {
//   id: 5,
//   name: "CBS",
//   score: "???",
//   url: "http://google.com"
// }]

App.Bar.FIXTURES = []

$(function () {
  $('body').popover({
      selector: '[data-toggle=popover]',
      trigger:  'hover'
  });
});
