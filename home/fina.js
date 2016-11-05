
function tableCellGet(myClass, x, y){
  var jqstr = myClass + ' tbody tr:nth-child(' + y + ') td:nth-child(' + x + ')';
  return $(jqstr).html()
}

function tableCellSet(myClass, x, y, myVal){
  var jqstr = myClass + ' tbody tr:nth-child(' + y + ') td:nth-child(' + x + ')';
  $(jqstr).html(myVal);
}

function catAreaUpdate(){
  $.ajax({
    'url' : 'api/trans',
    'type' : 'GET',
    'data' : { cat: ''},
    'success' : function(data){
      if(data == ''){
        $('.catInput').hide();
      } 
      $('.catArea').html(data);
    }
  });
}

function transAreaUpdate(){
  $.ajax({
    'url' : 'api/trans',
    'type'  :  'GET',
    'success' : function(data){
        $('.transArea').html(data);
    }  
  });
}

function graphUpdate(gType){
  var now = new Date().getTime();
  $('.graphImage').attr('src', '/api/trans?graph=' + gType + "&now=" + now);
}

function updateAll(){
  catAreaUpdate();
  transAreaUpdate();
  graphUpdate('pareto');
}
  

$(document).ready(function(){

  Dropzone.options.ofxFileDropzone = {
    paramName:  "tFile",
    maxFilesize:  2,
    method:  "put",
    accept:  function(file, done) {
               done();
             },
    complete:  function(){
             updateAll();
           }
  };

  updateAll();

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

  $('input[name=newCat]').keypress(function(e) {
    if(e.which == 13){
      $.ajax({
        'url' : 'api/trans',
        'type' : 'POST',
        'data' : {
                   cat:  $('input[name=newCat]').val(),
                   payee: tableCellGet('.payeeTable', 2, 1)
                 },
        'success' : function(data){
          updateAll();
        }
      });
      $('input[name=newCat]').val('');
    }
  });
});
