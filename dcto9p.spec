Summary:	Thomson TO9+ emulator
Name:		dcto9p
Version:	11.0
Release:	3
License:	GPLv3+
Group:		Emulators
Url:		http://dcto9p.free.fr/
Source0:	http://dcto9p.free.fr/v11/download/%{name}v%{version}.tar.gz
Source1:	%{name}-32.png
Source2:	%{name}-16.png
Patch0:		dcto9pv11.0-user_directory.patch.bz2
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_ttf)

%description
DCTO9+ is an emulator for the Thomson TO9+ system.

%files
%doc licence/dcto9pv11-licence.txt licence/gpl-3.0.txt licence/lgpl-3.0.txt licence/vera-copyright.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

#----------------------------------------------------------------------------

%prep
%setup -q -c %{name}-%{version}-%{release}
%patch0 -p0
sed -i s/cc/"gcc %{optflags}"/g makefile

%build
%make

%install
# binary
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 dcto9p %{buildroot}%{_bindir}/

# icon
install -d -m 755 %{buildroot}%{_iconsdir}
install -m 644 %{SOURCE1} %{buildroot}%{_iconsdir}/%{name}.png
install -d -m 755 %{buildroot}%{_liconsdir}
install -m 644 %{SOURCE2} %{buildroot}%{_liconsdir}/%{name}.png

# xdg menu
install -d -m 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=DCTO9+
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;Emulator;
EOF

