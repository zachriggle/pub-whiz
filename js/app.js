// Ember.ENV.EXPERIMENTAL_CONTROL_HELPER = true;
// Ember.LOG_BINDINGS = true;
// Ember.ENV.RAISE_ON_DEPRECATION = true
// Ember.LOG_STACKTRACE_ON_DEPRECATION = true

window.App = Ember.Application.create({
    rootElement: '#app',
    // LOG_TRANSITIONS: true
});

App.Router.map(function() {
  this.resource('bar', function() {
      this.resource('bar', {path:':bar_id'});
  });
});

App.ApplicationRoute = Ember.Route.extend({
  setupController: function(controller) {
    this.controllerFor('nav').set('content', App.Bar.find());
  },  
  renderTemplate: function() {
    this.render();
    this.render("nav", {outlet: "nav", into: "application"})
  }
});

App.BarRoute = Ember.Route.extend({
    model: function(params) {
        return App.Bar.find(params.bar_id);
    }
});

App.ApplicationController = Ember.Controller.extend({
  routeChanged: (function() {
    if (!window._gaq) {
      return;
    }
    return Em.run.next(function() {
      _gaq.push(['_trackPageview']);
    });
  }).observes('currentPath')
})

App.NavController = Ember.ArrayController.extend({
});


App.BarController = Ember.ObjectController.extend({
  sortedBeers: (function () {
    return Ember.ArrayProxy.createWithMixins(Ember.SortableMixin, {
      sortProperties: ['score'],
      content: this.get('content.beers'),
      sortAscending: false
    })
  }).property('content.beers')
});

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

App.Beer.FIXTURES = []
App.Bar.FIXTURES = []

$(function () {
  $('body').popover({
      selector: '[data-toggle=popover]',
      trigger:  'hover'
  });
});
