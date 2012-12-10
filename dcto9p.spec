Name:			dcto9p
Version:		11.0
Release:		%mkrel 2

Summary:	Thomson TO9+ emulator
Group:		Emulators
License:	GPLv3+
URL:		http://dcto9p.free.fr/
Source0:	http://dcto9p.free.fr/v11/download/%{name}v%{version}.tar.gz
Source1:	%{name}-32.png
Source2:	%{name}-16.png
Patch0:		dcto9pv11.0-user_directory.patch.bz2
BuildRequires:  SDL-devel
BuildRequires:  SDL_ttf-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}


%description
DCTO9+ is an emulator for the Thomson TO9+ system.

This package is in PLF because of Mandriva policy concerning emulators.

%prep
%setup -q -c %{name}-%{version}-%{release}
%patch0 -p0

%build
%make

%install
rm -rf %{buildroot}
# binary
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 dcto9p %{buildroot}%{_bindir}/
# icon
install -d -m 755 %{buildroot}%{_iconsdir}
install -m 644 %{_sourcedir}/%{name}-32.png %{buildroot}%{_iconsdir}/%{name}.png
install -d -m 755 %{buildroot}%{_liconsdir}
install -m 644 %{_sourcedir}/%{name}-16.png %{buildroot}%{_liconsdir}/%{name}.png
# xdg menu
install -d -m 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=DCTO9+
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Emulators;Emulator;
EOF

%files
%defattr(-,root,root)
%doc documentation/dcto9pv11.css documentation/dcto9pv11en.html documentation/dcto9pv11fr.html documentation/index.html licence/dcto9pv11-licence.txt licence/gpl-3.0.txt licence/lgpl-3.0.txt licence/vera-copyright.txt
%{_bindir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop

%clean
rm -rf %{buildroot}



%changelog
* Tue Aug 02 2011 Andrey Bondrov <abondrov@mandriva.org> 11.0-2mdv2012.0
+ Revision: 692803
- imported package dcto9p


* Sun Nov 09 2008 Guillaume Rousse <guillomovitch@zarb.org> 11.0-1plf2009.1
- contributed by Jean-Christophe Cardot (<plf@cardot.net>)
