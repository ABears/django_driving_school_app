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
      {
          days: ['2019-03-22'],
          backgroundColor: '#f08080',
          title: 'Dad Birthday'
      },
      {
          days: ['2019-12-18'],
          backgroundColor: '#f08080',
          title: 'Mom Birthday'
      }
  ],
    onLoad: () => {

      calendar.setDaysHighlight([
        {days: ['2019-06-01'],backgroundColor: '#f08080'},
      ]);
      calendar.update();

    },
    onChange: updateInfo,
    onSelect: updateInfo
  //   onClear: updateInfo
    
  });

  const today = document.querySelector('.demo-today');
  const picked = document.querySelector('.demo-picked');
  const last = document.querySelector('.demo-last');

  function updateInfo() {

      
      if (this.today) {
          today.innerHTML = '';
          var li = document.createElement('li');
          li.innerHTML = this.today;
          today.appendChild(li);
      }

      if (this.lastSelectedDay) {

          last.innerHTML = '';
          var li = document.createElement('h2');
          li.innerHTML += new Date(this.lastSelectedDay).getDate() + '/';
          li.innerHTML += Number(new Date(this.lastSelectedDay).getMonth()) + 1;
          li.innerHTML += '/' + new Date(this.lastSelectedDay).getFullYear();
          last.appendChild(li);

      }
      
  }
  
  $('.add-appointement').click(function(){
    let getRow  = this.parentNode.parentNode.previousElementSibling;
    let getHour = getRow.childNodes[1].innerHTML;

    let appointement = last.firstChild.innerHTML + ' ' + getHour + ':00:00';
    let userId = document.querySelector('.user-token').getAttribute("data-user");
    let studentId = document.querySelector('.student-selector').value;
    let instructorId = document.querySelector('.instructor-selector').value;
    let createAppointementUrl = '/create-appointement/'  + userId + '/' + studentId + '/' + instructorId;
    let token  = document.querySelector('.get-csrf').childNodes[1].value;
    let data = { appointement, csrfmiddlewaretoken: token };

    console.log(token);

    $.ajax({
      type: "POST",
      url: createAppointementUrl,
      data: data,
      success: function(response) {
        console.log(response);
      }
    })

  });