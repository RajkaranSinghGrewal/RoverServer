async function updateValueFromApi(){
		try{
			const response = await fetch("http://10.0.0.25/data");
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
			document.getElementById('voc_index_valueValue').innerText = updatedValue.voc_index_value;
			document.getElementById('adc_rawValue').innerText = updatedValue.adc_raw;
			console.log('Updated value:', updatedValue);
			updateValueFromApi();
			}
			else{
				throw new Error('Response is not in JSON format');
			}
		}catch (error){
			console.error('Error',error.message);
		}
	}
updateValueFromApi();
