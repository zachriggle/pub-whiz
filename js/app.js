Ember.ENV.EXPERIMENTAL_CONTROL_HELPER = true;

window.App = Ember.Application.create({
    rootElement: '#app'
});

App.Router.map(function() {
  this.resource('bars', function() {
      this.resource('bar', {path:':bar_id'});
  });
  this.route("about", {path: '/about'})
});

App.IndexRoute = Ember.Route.extend({
    redirect: function() {
        this.transitionTo('bars'); 
    }
});

App.ApplicationRoute = Ember.Route.extend({
    setupController: function() {
        this.controllerFor('bar').set('model', App.Bar.find());
    }
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

App.LinkView = Ember.View.extend({
  tagName: 'a',
  attributeBindings: ['href']
})

App.Store = DS.Store.extend({
      revision: 12,
      adapter: DS.FixtureAdapter.create()
});

App.Beer = DS.Model.extend({
  name:  DS.attr('string'),
  score: DS.attr('string'),
  url:   DS.attr('string'),
  bar:  DS.belongsTo('App.Bar')
});

App.Bar = DS.Model.extend({
  name: DS.attr('string'),
  description: DS.attr('string'),
  beers: DS.hasMany('App.Beer'),
  url:   DS.attr('string')
});

App.BarDescriptionController = Ember.ObjectController.extend();


App.BeersController = Ember.ArrayController.extend();

App.register('controller', 'beerItem', App.BeerController);

App.BarController = Ember.ArrayController.extend({
  itemController: 'beerItem'
});

App.register('controller', 'barItem', App.BarController);

App.BarsController = Ember.ArrayController.extend({
  itemController: 'barItem',
  beers: (function() {
    return Ember.ArrayProxy.createWithMixins(Ember.SortableMixin, {
      sortProperties: ['rating'],
      content: this.get('content.beers')
    })
  }).property('content.beers')
});

App.Beer.FIXTURES = [{
  id: 1,
  name: "Pliny the Younger",
  score: "100",
  url: "#",
  bar: 1
}, {
  id: 2,
  name: "Pliny the Elder",
  score: "20",
  url: "#",
  bar: 1
}, {
  id: 3,
  name: "Hopslam",
  score: "99",
  url: "#"
}, {
  id: 4,
  name: "KBS",
  score: 97,
  url: "http://google.com"
}]

App.Bar.FIXTURES = [{
  id: 1,
  name: "Maxs",
  description: "Max's Taphouse is Baltimore's premier beer pub. Max's is in the heart of historic Fells Point, just east of the Inner Harbor at Water Taxi Stop #11. With 140 ...",
  beers: [1,2],
  url: "http://maxs.com"
}, {
  id: 2,
  name: "Frisco",
  description: "It's a grille!",
  beers: [3,4],
  url: "http://friscogrille.com"
}]


$(function () {
  $('body').popover({
      selector: '[data-toggle=popover]',
      trigger:  'hover'
  });
});