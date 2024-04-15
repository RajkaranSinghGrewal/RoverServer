async function updateValueFromApi(){
	ip_address = "http://192.168.50.25/"	
	try{
		const response = await fetch("/controller/data");
		if(!response.ok){
			throw new Error('Failed to fetch data from api');
		}
		const contentType = response.headers.get('content-type');	
		if(contentType && contentType.includes('application/json')){

			const data = await response.json();
			console.log('Data:',data);

			const updatedValue = data.value;
			document.getElementById('tempValue').innerText = updatedValue.temp;
			document.getElementById('humValue').innerText = updatedValue.hum;
			document.getElementById('vocValue').innerText = updatedValue.voc;
			document.getElementById('adc_rawValue').innerText = updatedValue.adc_raw;
			console.log('Updated value:', updatedValue);
			
		}
		else{
			throw new Error('Response is not in JSON format');
		}
	}catch (error){
		console.error('Error',error.message);
	}
}

setInterval(() => {
updateValueFromApi();},1000);
