package ml.backend.controller;

import lombok.extern.slf4j.Slf4j;
import org.apache.tomcat.util.codec.binary.Base64;
import org.apache.tomcat.util.codec.binary.StringUtils;
import org.springframework.http.*;
import org.springframework.stereotype.Controller;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.HttpServletRequest;
import java.io.IOException;
import java.util.HashMap;

@Controller
@Slf4j
@RequestMapping("/test")
public class ViewController {

    @GetMapping("/image")
    public String imageView() {
        return "main";
    }

    @PostMapping("/image")
    public String imageUpload(String image) throws IOException {
        image = image.substring(image.lastIndexOf("base64,")+7);
        log.info(image);

//        StringBuilder sb = new StringBuilder();
//        sb.append(StringUtils.newStringUtf8(Base64.encodeBase64(image.getBytes(), false)));

        MultiValueMap<String, String> params = new LinkedMultiValueMap<>();
        params.add("content", image);

        HttpHeaders headers = new HttpHeaders();
        headers.add("Content-Type", "application/json");
        headers.add("Accept", "application/json");
        headers.add("Accept-Encoding", "gzip, deflate, br");

        HttpEntity<MultiValueMap<String, String>> entity = new HttpEntity<>(params, headers);

        RestTemplate rt = new RestTemplate();

        try {
            ResponseEntity<String> response = rt.exchange(
                    "http://localhost:8000/api/face/",
                    HttpMethod.POST,
                    entity,
                    String.class
            );
            log.info(response.getBody());
        } catch (Exception e) {
            log.warn(e.toString());
        }

        return "redirect:/test/image";
    }

    @GetMapping("/cam")
    public String liveCamView() {
        return "cam";
    }

}