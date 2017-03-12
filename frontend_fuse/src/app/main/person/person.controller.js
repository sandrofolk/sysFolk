(function(){
    'use strict';

    angular
        .module('app.person')
        .controller('PersonController', PersonController)


    function PersonController(persons, $state){
        var vm = this;
        vm.dataService = persons

        vm.goAddPerson = function(){
            $state.go('app.person.form')
        }
        vm.goEditPerson = function(dataObject){
            $state.go('app.person.form',{
                id: dataObject.id,
            })
        }

        vm.dtOptions = {
            dom         : 'rt<"bottom"<"left"<"length"l>><"right"<"info"i><"pagination"p>>>',
            initComplete: function ()
            {
                var api = this.api(),
                    searchBox = angular.element('body').find('#e-commerce-products-search');

                // Bind an external input as a table wide search box
                if ( searchBox.length > 0 )
                {
                    searchBox.on('keyup', function (event)
                    {
                        api.search(event.target.value).draw();
                    });
                }
            },
            pagingType  : 'simple',
            lengthMenu  : [10, 20, 30, 50, 100],
            pageLength  : 20,
            scrollY     : 'auto',
            responsive  : true
        };

    }

}());