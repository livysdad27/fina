function tableCellGet(myClass, x, y){
  var jqstr = myClass + ' tbody tr:nth-child(' + y + ') td:nth-child(' + x + ')';
  return $(jqstr).html()
}

function tableCellSet(myClass, x, y, myVal){
  var jqstr = myClass + ' tbody tr:nth-child(' + y + ') td:nth-child(' + x + ')';
  $(jqstr).html(myVal);
}

$(document).ready(function(){

  var now = new Date();

  var nowStr = now.getFullYear() + '-' 
             + ('00' + (now.getMonth() + 1)).slice(-2) + '-' 
             + ('00' + now.getDate()).slice(-2) + 'T' 
             + ('00' + now.getHours()).slice(-2) + ':'
             + ('00' + now.getMinutes()).slice(-2); 
//  $('input[name=startDate]').val("2016-01-01T00:00:00");
//  $('input[name=endDate]').val(nowStr);
  $.ajax({
    'url' : 'api/trans',
    'type' : 'GET',
    'data' : { cat: ''},
    'success' : function(data){
      $('.catArea').html(data);
    }
  });

  $('button[name=queryButton]').click(function() {
    $.ajax({
      'url' : 'api/trans',
      'type'  :  'GET',
      'data' :  {
                  startDate:  $('input[name=startDate]').val(),
                  endDate:  $('input[name=endDate]').val()
                 },
      'success' : function(data){
          $('.transArea').html(data);
      }  
    });
  });

  $('button[name=updateCat]').click(function() {
    $.ajax({
      'url' : 'api/trans',
      'type' : 'POST',
      'data' : {
                 cat:  $('input[name=newCat]').val(),
                 payee: tableCellGet('.payeeTable', 2, 1)
               },
      'success' : function(data){
        $.ajax({
          'url' : 'api/trans',
          'type' : 'GET',
          'data' : { cat: ''},
          'success' : function(data){
            $('.catArea').html(data);}
        });
      }
    });
  });
});
