package ml.backend.controller;

import lombok.extern.slf4j.Slf4j;
import org.apache.tomcat.util.codec.binary.Base64;
import org.apache.tomcat.util.codec.binary.StringUtils;
import org.springframework.http.*;
import org.springframework.stereotype.Controller;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.HttpServletRequest;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;

@Controller
@Slf4j
@RequestMapping("/test")
public class ViewController {

    @GetMapping("/image")
    public String imageView() {
        return "main";
    }

    @PostMapping("/image")
    @ResponseBody
    public ArrayList<Integer> imageUpload(String image) throws IOException {
        image = image.substring(image.lastIndexOf("base64,")+7);

        MultiValueMap<String, String> params = new LinkedMultiValueMap<>();
        params.add("content", image);

        HttpHeaders headers = new HttpHeaders();
        headers.add("Content-Type", "application/json");
        headers.add("Accept", "application/json");
        headers.add("Accept-Encoding", "gzip, deflate, br");

        HttpEntity<MultiValueMap<String, String>> entity = new HttpEntity<>(params, headers);

        RestTemplate rt = new RestTemplate();

        try {
            ResponseEntity<LinkedHashMap> response = rt.postForEntity(
                    "http://localhost:8000/api/face/",
                    entity,
                    LinkedHashMap.class
            );
            ArrayList<Integer> result = (ArrayList<Integer>) response.getBody().get("result");
            log.info("result: " + result.toString());
            return result;
        } catch (Exception e) {
            log.warn(e.toString());
        }
        return null;
    }

    @GetMapping("/cam")
    public String liveCamView() {
        return "cam";
    }

}