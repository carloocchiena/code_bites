import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;

public class FileString {

    public static void main(String[] args) throws IOException {

        String path = System.getProperty("user.dir") + "\\src\\test.txt";
        Charset encoding = Charset.defaultCharset();

        byte[] encoded = Files.readAllBytes(Paths.get(path));
        String lines = new String(encoded, encoding);
        System.out.println(lines);
    }
}
