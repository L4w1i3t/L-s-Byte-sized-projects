document.addEventListener('DOMContentLoaded', () => {
    const distanceChoice = document.getElementById('distanceChoice');
    const customDistanceDiv = document.getElementById('customDistanceDiv');
    const paceForm = document.getElementById('paceForm');
    const resultDiv = document.getElementById('result');
  
    distanceChoice.addEventListener('change', () => {
      customDistanceDiv.classList.toggle('hidden', distanceChoice.value !== 'custom');
    });
  
    paceForm.addEventListener('submit', (e) => {
      e.preventDefault();
  
      // Determine distance (in kilometers)
      let distance = parseFloat(distanceChoice.value);
      if (distanceChoice.value === 'custom') {
        const customDistance = parseFloat(document.getElementById('customDistance').value);
        if (isNaN(customDistance) || customDistance <= 0) {
          resultDiv.textContent = 'Please enter a valid custom distance.';
          return;
        }
        const customUnit = document.getElementById('customDistanceUnit').value;
        distance = customUnit === 'miles' ? customDistance * 1.60934 : customDistance;
      }
  
      // Get pace unit selection
      const paceUnit = document.getElementById('paceUnit').value;
  
      // Get time input
      const hours = parseInt(document.getElementById('hours').value) || 0;
      const minutes = parseInt(document.getElementById('minutes').value) || 0;
      const seconds = parseInt(document.getElementById('seconds').value) || 0;
      if (minutes < 0 || minutes >= 60 || seconds < 0 || seconds >= 60) {
        resultDiv.textContent = 'Invalid time entered. Please check minutes and seconds.';
        return;
      }
      const totalSeconds = hours * 3600 + minutes * 60 + seconds;
  
      // Adjust distance for pace calculation if needed
      if (paceUnit === 'miles') {
        distance = distance / 1.60934; // convert km to miles
      }
  
      if (distance <= 0) {
        resultDiv.textContent = 'Invalid distance for calculation.';
        return;
      }
  
      // Calculate pace (seconds per unit)
      const paceInSeconds = totalSeconds / distance;
      const paceMinutes = Math.floor(paceInSeconds / 60);
      const paceSeconds = Math.round(paceInSeconds % 60);
  
      resultDiv.textContent = `You need to run at an average pace of ${paceMinutes} minutes and ${paceSeconds} seconds per ${paceUnit === 'km' ? 'kilometer' : 'mile'}.`;
    });
  });
  