const token = document.querySelector('.get-csrf').childNodes[1].value;

const calendar = new HelloWeek({
    selector: '.hello-week',
    lang: 'en',
    langFolder: '/static/hello-week-master/dist/langs/',
    format: 'dd/mm/yyyy',
    weekShort: true,
    monthShort: false,
    multiplePick: false,
    defaultDate: false,
    todayHighlight: true,
    daysSelected: null,
    disablePastDays: true,
    disabledDaysOfWeek: false,
    disableDates: false,
    weekStart: 0, // 0 (Sunday) to 6 (Saturday).
    daysHighlight: true,
    range: false,
    rtl: false,
    locked: false,
    minDate: false,
    maxDate: false,
    nav: ['◀', '▶'],
    daysHighlight: [
  ],
    onLoad: () => {
      
      reloadAppointement();

    },
    onChange: updateInfo,
    onSelect: updateInfo
  //   onClear: updateInfo
    
  });

  const today = document.querySelector('.demo-today');
  const picked = document.querySelector('.demo-picked');
  const last = document.querySelector('.demo-last');
  const getSubjectUserId = document.querySelector('.user-container').getAttribute('data-subject-user');

  String.prototype.replaceAll = function(target, replacement) {
    return this.split(target).join(replacement);
  };

  $('#day-planning').hide()

  function updateInfo() {

      $('#day-planning').show()

      if (this.today) {
          today.innerHTML = '';
          var li = document.createElement('li');
          li.innerHTML = this.today;
          today.appendChild(li);
      }

      if (this.lastSelectedDay) {

          last.innerHTML = '';
          var li = document.createElement('h2');
          li.classList.add('get-current-day');
          li.innerHTML += new Date(this.lastSelectedDay).getDate() + '/';
          li.innerHTML += Number(new Date(this.lastSelectedDay).getMonth()) + 1;
          li.innerHTML += '/' + new Date(this.lastSelectedDay).getFullYear();
          last.appendChild(li);

          let fullDate = li.innerHTML

          getDayPlanning(fullDate.replaceAll('/', '-'));

      }

  }

  
  function getDayPlanning(fullDate){

    let getDayPlanningUrl = '/read-day-planning/' + getSubjectUserId  + '/' + fullDate;
    let data = {csrfmiddlewaretoken: token };

    $.ajax({
      type: "GET",
      url: window.location.href,
      success: function(response) {

        let reloadedCalendar = $(response).find('#day-planning').html();
        $('#day-planning').html(reloadedCalendar);
        
      }
    })
    .then(() => {
      
      let getUserBaseUrl = '/read-user/';

      $.ajax({
        type: "POST",
        url: getDayPlanningUrl,
        data: data,
        success: function(response) {
  
          const allAppointement = response.all_appointement;
  
          for (let key in allAppointement){
            
            let appointement = allAppointement[key];

            $.ajax({
              type: "POST",
              url: getUserBaseUrl + appointement.instructor_id,
              data: data,
              success: function(response) {
                
                getInstructor = response.subject_user[0].last_name + ' ' + response.subject_user[0].first_name;
                
              }
            })
            .then(() => {
              $.ajax({
                type: "POST",
                url: getUserBaseUrl + appointement.student_id,
                data: data,
                success: function(response) {
  
                  getStudent = response.subject_user[0].last_name + ' ' +response.subject_user[0].first_name;
  
                }
              }).then(() => {
                  let getHour = new Date(appointement.appointement_date).getUTCHours();
              
                  $('.r-' + getHour).attr('data-appointement-datetime', appointement.id);
                  $('.r-' + getHour).html('');
        
                  $('.r-' + getHour).parent().addClass('bg-danger');
                  $('.r-' + getHour).html('<div class="p-5 text-center">' + getInstructor + ' / ' + getStudent + '</div>');
                  $('.r-' + getHour).next().html('<button class="img text-light h6 btn btn-circle btn-xl btn-danger delete-appointement" ><i class="fa fa-trash"></i></button>'); 
      
                  $('.delete-appointement').click(function(){
                    deleteAppointement($(this));
                  });
              })
            })
          }
  
        }
      })

    })
    .then(() =>{

      $('.add-appointement').click(function(){

        let getRow  = this.parentNode.parentNode.previousElementSibling;
        setAppointment(getRow);
    
        $('.alert').click(function(){
          this.slideUp();
        });
    
      });

    })
    
  }

  function reloadAppointement(){

    let getAppointementUrl = '/read-appointement/'  + getSubjectUserId ;
    let data = {csrfmiddlewaretoken: token }
    let bookedAppointement = []

    $.ajax({
      type: "POST",
      url: getAppointementUrl,
      data: data,
      success: function(response) {

        const allAppointement = response.all_appointement;

        for (let key in allAppointement){

          let appointement = allAppointement[key];
          appointementFormatDate = '';
          appointementFormatDate +=  new Date(appointement.appointement_date).getFullYear() + '-';

          if(Number(new Date(appointement.appointement_date).getMonth()) + 1 < 10){
            appointementFormatDate += '0';
          }

          appointementFormatDate +=  Number(new Date(appointement.appointement_date).getMonth()) + 1;
          appointementFormatDate += '-' + new Date(appointement.appointement_date).getDate();

          bookedAppointement[key] = appointementFormatDate

        }

      }
    }).then(() =>{

      calendar.setDaysHighlight([
        {days: bookedAppointement, backgroundColor: '#f08080'},
      ]);

      calendar.update();  
    })

  }


  function setAppointment(getRow){

    let getHour = getRow.childNodes[1].innerHTML;

    let appointement = last.firstChild.innerHTML + ' ' + getHour + ':00:00';
    let userId = document.querySelector('.user-token').getAttribute("data-user");
    let studentId = $('.student-selector').val();
    let instructorId = $('.instructor-selector').val();
    let createAppointementUrl = '/create-appointement/'  + userId + '/' + studentId + '/' + instructorId;
    let data = { appointement, csrfmiddlewaretoken: token };

    $.ajax({
      type: "POST",
      url: createAppointementUrl,
      data: data,
      success: function(response) {
        if(response.success){
          
          let fullDate = $('.get-current-day').html()
          console.log(fullDate);
          getDayPlanning(fullDate.replaceAll('/', '-'))

          $('.' + getHour).addClass('d-none');
          $('.' + getHour).removeClass('alert-danger');
          $('.' + getHour).removeClass('alert-success');
          $('.' + getHour).removeClass('d-none');
          $('.' + getHour).addClass('alert-success');
          $('.' + getHour).text(response.success);

          $('.r-' + getHour).html('');

          $('.r-' + getHour).parent().addClass('bg-danger');
          $('.r-' + getHour).next().html('<button class="img text-light h6 btn btn-circle btn-xl btn-danger delete-appointement" ><i class="fa fa-trash"></i></button>');

        }
        else if (response.error){

          $('.' + getHour).addClass('d-none');
          $('.' + getHour).removeClass('alert-danger');
          $('.' + getHour).removeClass('alert-success');
          $('.' + getHour).removeClass('d-none');
          $('.' + getHour).addClass('alert-danger');
          $('.' + getHour).text(response.error);

          $('.delete-appointement').click(function(){
            deleteAppointement($(this));
          });

        }
      }
    }).then(() => {
      reloadAppointement();
    })

  }

// Event functions //

// Add appointement event
  $('.add-appointement').click(function(){

    let getRow  = this.parentNode.parentNode.previousElementSibling;
    setAppointment(getRow);

    $('.alert').click(function(){
      this.slideUp();
    });

  });

function deleteAppointement(trigger){
  let appointementRow = trigger.parent().prev();
  console.log(appointementRow);
  let getAppointemenId = appointementRow.attr('data-appointement-datetime');

  let getAppointementUrl = "/delete-appointement/"+ getSubjectUserId + '/' + getAppointemenId
  
  $.ajax({
    type: "POST",
    url: getAppointementUrl,
    data: {csrfmiddlewaretoken: token},
    success: function(response) {;
      
    }

  })
  .then(() => {

    $.ajax({
      type: "GET",
      url: window.location.href,
      success: function(response) {

        let reloadedCalendar = $(response).find('.col-lg-9').html();
        appointementRow.parent().removeClass('bg-danger')
        appointementRow.parent().html(reloadedCalendar);
        
      }
    })
    .then(() => {

      $('.add-appointement').click(function(){

        let getRow  = this.parentNode.parentNode.previousElementSibling;
        setAppointment(getRow);
    
        $('.alert').click(function(){
          this.slideUp();
        });
    
      });

      
    })

  })

}